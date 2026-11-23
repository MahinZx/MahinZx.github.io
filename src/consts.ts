import type { Site, Page, Links, Socials } from "@types"
export const SITE: Site = {
  TITLE: "Mahin",
  DESCRIPTION: "Mahin is an Information Technologies student at VILNIUS TECH building software, exploring systems, and asking questions about the cosmos.",
  AUTHOR: "Mahin",
}
export const WORK: Page = { TITLE: "Work", DESCRIPTION: "Places I've worked and what I've learned." }
export const BLOG: Page = { TITLE: "Notes", DESCRIPTION: "Writing about the things I'm learning." }
export const PROJECTS: Page = { TITLE: "Projects", DESCRIPTION: "University projects and personal experiments." }
export const SEARCH: Page = { TITLE: "Search", DESCRIPTION: "Search notes and projects." }
export const LINKS: Links = [
  { TEXT: "Home", HREF: "/" },
  { TEXT: "Work", HREF: "/work" },
  { TEXT: "Notes", HREF: "/blog" },
  { TEXT: "Projects", HREF: "/projects" },
]
export const SOCIALS: Socials = [
  { NAME: "Email", ICON: "email", TEXT: "abdullahalmahinbhuiyan@gmail.com", HREF: "mailto:abdullahalmahinbhuiyan@gmail.com" },
  { NAME: "Github", ICON: "github", TEXT: "MahinZx", HREF: "https://github.com/MahinZx" },
]
