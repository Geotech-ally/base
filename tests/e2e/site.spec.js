const { test, expect } = require('@playwright/test');
const AxeBuilder = require('@axe-core/playwright').default;

test('loads the homepage and primary navigation', async ({ page }) => {
  await page.goto('/');
  await expect(page).toHaveTitle(/Nuru Tech/);
  await expect(page.getByRole('heading', { level: 1 })).toBeVisible();
  await expect(page.getByRole('navigation', { name: 'Primary' })).toBeVisible();
});

test('filters portfolio projects', async ({ page }) => {
  await page.goto('/#portfolio');
  await page.getByRole('button', { name: 'Web Apps' }).click();
  await expect(page.getByText(/Showing 2 of 6 projects in Web Apps/)).toBeVisible();
  await expect(page.locator('.project-card:not([hidden])')).toHaveCount(2);
});

test('validates the demonstration form', async ({ page }) => {
  await page.goto('/#contact');
  await page.getByRole('button', { name: 'Send message' }).click();
  await expect(page.getByText(/Please fix 5 fields below/)).toBeVisible();
});

test('has no automatically detectable serious accessibility violations', async ({ page }) => {
  await page.goto('/');
  const results = await new AxeBuilder({ page }).analyze();
  const serious = results.violations.filter((violation) =>
    ['serious', 'critical'].includes(violation.impact)
  );
  expect(serious).toEqual([]);
});
