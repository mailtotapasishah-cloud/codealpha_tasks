
export const metadata = {
  title: 'AI Language Translator',
  description: 'Modern Language Translation Tool'
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
