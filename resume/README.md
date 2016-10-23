# Resume Template

Template for a Curriculum Vitae or Resume. Recommended compiler is LuaLaTeX.

## Commands

### Sections

`\section` and `\subsection` command have been stylised accordingly.

### Header

A smart header with links, FontAwesome icons and anything else you want under the heading can be input using the `\header` command. For example:

```latex
\header{John Smith}{
  \href{mailto:john.smith@gmail.com}{\faEnvelope\hspace{1mm}john.smith@gmail.com}
  \hspace{4mm}
  \href{https://www.linkedin.com/in/johnsmith}{\faLinkedin\hspace{1mm}linkedin.com/in/johnsmith}
}
```

### Entry list

Creates an environment with a thin date column on the left and a larger description column on the right. Entries can be added using the the `\entry` command which will add a date, heading and location with a description underneath. For example to add a two entry list for experience:

```latex
\begin{entrylist}
  \entry
    {Mon Year -- Mon Year}
    {Company | Location}
    {Job Title}
    {Explanation of responsibilities, what you achieved etc}
  \entry
    {Mon Year -- Mon Year}
    {Company | Location}
    {Job Title}
    {Explanation of responsibilities, what you achieved etc}
\end{entrylist}
```
