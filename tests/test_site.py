from html.parser import HTMLParser
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.labels = []
        self.images = []
        self.local_refs = []
        self.h1_count = 0
        self.headings = []
        self.anchor_targets = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.append(attrs["id"])
        if tag == "label" and attrs.get("for"):
            self.labels.append(attrs["for"])
        if tag == "img":
            self.images.append(attrs)
        if tag == "h1":
            self.h1_count += 1
        if re.fullmatch(r"h[1-6]", tag):
            self.headings.append(tag)
        for attr in ("href", "src"):
            value = attrs.get(attr)
            if value and not value.startswith(("#", "http:", "https:", "mailto:", "tel:", "data:")):
                self.local_refs.append(value.split("?", 1)[0])
            if attr == "href" and value and value.startswith("#") and len(value) > 1:
                self.anchor_targets.append(value[1:])


class SiteTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = (ROOT / "index.html").read_text(encoding="utf-8")
        cls.parser = SiteParser()
        cls.parser.feed(cls.html)

    def test_one_h1_and_semantic_title(self):
        self.assertEqual(self.parser.h1_count, 1)
        self.assertIn("<title>", self.html)
        self.assertIn("<meta name=\"description\"", self.html)

    def test_duplicate_ids_are_absent(self):
        duplicates = {item for item in self.parser.ids if self.parser.ids.count(item) > 1}
        self.assertEqual(duplicates, set())

    def test_form_labels_reference_fields(self):
        for field_id in self.parser.labels:
            self.assertIn(field_id, self.parser.ids)

    def test_images_have_alt_and_dimensions(self):
        for image in self.parser.images:
            self.assertIn("alt", image)
            self.assertIn("width", image)
            self.assertIn("height", image)

    def test_local_assets_exist(self):
        missing = []
        for ref in self.parser.local_refs:
            if not (ROOT / ref).exists():
                missing.append(ref)
        self.assertEqual(missing, [])

    def test_navigation_targets_exist(self):
        targets = set(self.parser.anchor_targets)
        missing = targets - set(self.parser.ids)
        self.assertEqual(missing, set())

    def test_seo_metadata_is_present(self):
        self.assertIn('property="og:title"', self.html)
        self.assertIn('property="og:description"', self.html)
        self.assertIn('property="og:type"', self.html)
        self.assertIn('name="robots"', self.html)

    def test_deployment_and_search_files_exist(self):
        for relative in ("robots.txt", "sitemap.xml", ".nojekyll", "LICENSE"):
            self.assertTrue((ROOT / relative).exists())

    def test_workflows_use_expected_actions(self):
        pages = (ROOT / ".github/workflows/pages.yml").read_text(encoding="utf-8")
        self.assertIn("actions/upload-pages-artifact@v3", pages)
        self.assertIn("actions/deploy-pages@v4", pages)
        self.assertIn("pages: write", pages)
        ci = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
        self.assertIn("pull_request:", ci)
        self.assertIn("branches: [main]", ci)

    def test_confirmed_business_and_license_details(self):
        self.assertIn("hello@nurutech.ac.ke", self.html)
        self.assertIn("0768998191", self.html)
        self.assertIn("Bondo, Kenya", self.html)
        license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
        self.assertIn("Apache License", license_text)


if __name__ == "__main__":
    unittest.main()
