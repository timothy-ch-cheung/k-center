import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders learn react link', () => {
  render(<App />);
  const paragraphElement = screen.getByText(/Colorful K-Center Clustering./i);
  expect(paragraphElement).toBeInTheDocument();
});
