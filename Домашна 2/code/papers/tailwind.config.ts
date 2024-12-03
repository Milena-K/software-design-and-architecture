import { type Config } from "tailwindcss";
import { fontFamily } from "tailwindcss/defaultTheme";

export default {
  content: ["./src/**/*.tsx"],
  theme: {
    extend: {
      fontFamily: {
        sans: ["var(--font-geist-sans)", ...fontFamily.sans],
      },
      colors: {
        'green': '#D8DBBD',
        'beige': '#FAF6E3',
        'brown': '#B59F78',
        'blue': '#2A3663',
      },
    },
  },
  plugins: [],
} satisfies Config;
