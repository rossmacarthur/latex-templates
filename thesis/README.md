# LaTeX Thesis Template

## General

This is a LaTeX template made for my undergraduate engineering thesis at the University of Cape Town. It is based on Mohohlo Tsoeu's report template for EEE4022S and John-Philip Taylor's report template for EEE4084F. The recommended compiler is pdfTeX or LuaTeX.

Basic global information such as author and thesis title can be changed in the `main.tex` file. The bibliography has been set to adhere to the IEEE standard and BibTeX entries can be placed in the References.bib file. Pages that are automatically included or setup in the template are: Cover page, Declaration, Abstract, Acknowledgments, Table of Contents, List of Figures, Code Listings, Nomenclature, Appendices.

## Commands

### Figures

Figures can be inserted using the `\Figure` command:

```latex
\Figure[width=1\columnwidth]{Example figure description}{figure_name}
```

This will create a figure with the caption "Example figure description" and a label with name `fig:figure_name`. `figure_name` must be the name of the figure, excluding extension, and should reside in the "figures" folder. The optional parameters that are given are directly passed to the `\includegraphics` command. In other words you can use other parameters such as `scale`, `angle`. For example a 90 degree rotated figure:

```latex
\Figure[width=1\columnwidth, angle=90]{Example figure description}{figure_name}
```

### Plots

LaTeX drawn plots using the PGFPlots package can be inserted using the `\Plot` command:

```latex
\Plot{Example plot description.}{plot_name}
```

This will create a drawn figure with the caption "Example plot description" and a label with name `fig:plot_name`. `plot_name` must be the name of the file, excluding the `.tex` extension, should reside in the "figures" folder and must contain a PGF plot. An example of what this file should contain is:

```latex
\begin{axis}[
  axis lines = left,
  xlabel = {Phase (radians)},
  ylabel = {Amplitude},
]
\addplot [
  domain=-pi:pi, 
  samples=1000,
  color=blue,
]
{sin(deg(x))};
\end{axis}
```

### Listings

You can insert syntax highlighted source code using:

```latex
\begin{lstlisting}[language=Matlab, caption={Code description}, label={lst:example_code}]
  # Example code
  x = linspace(0, 2*pi, 1000);
  y = sin(x);
  plot(x, y); grid on;
\end{lstlisting}
```
