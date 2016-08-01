# UCT Undergraduate Engineering Thesis Template

## General

This LaTeX template is based on Mohohlo Tsoeu's report template for EEE4022S and John-Philip Taylor's report template for EEE4084F. The recommended compiler is pdfLaTeX or LuaLaTeX.

Basic global information such as author and thesis title can be changed under the "Variables" heading in the `main.tex` file.


## New commands

All of these commands have been created for a much easier addition of figures, tables and source code entries into the document. 

### Figures

You can insert figures using the `\Figure` command as demonstrated below:

```latex
\Figure{Example figure description}{figurename}
```

This will create a floating figure with the caption "Example figure description" and a label with name `fig:figurename`. `figurename` must be the name of the excluding extension residing in the "figures" folder. The figure can be referenced in text like: 

```latex
see Figure~\ref{fig:figurename}
```

### Tables

You can insert tables using the `\Table` command as demonstrated below:

```latex
\Table{My Informative Table}{|l|c|r|}{ % this format specifies 3 columns with left, centre and right alignment
  \textbf{Heading 1} & \textbf{Heading 2} & \textbf{Heading 3}
}{
  Data & 123 & 321 \\
  Data & 456 & 654 \\
  Data & 789 & 987 \\
}{Example}
```

This will create a floating table with the caption "My Informative Table" and a label with name `tab:Example`. The table can be referenced in text like: 

```latex
see Table~\ref{tab:Example}    
```

### Listings

To include syntax highlighted source code in your document listing commands are set up. You can insert inline code:

```latex
\begin{Matlab}
  # Example code
  x = linspace(0, 2*pi, 1000);
  y = sin(x);
  plot(x, y); grid on;
\end{Matlab}
```

You can create a floating code listing:

```latex
\begin{Matlab_float}{Description of what this code is}{Matlab_code_example}
  x = linspace(0, 2*pi, 1000);
  y = sin(x);
  plot(x, y); grid on;
\end{Matlab_float}
```

This will create a listing with the caption "Description of what this code is" and a label with name "lst:Matlab_code_example". The listing can be referenced in text like:

```latex
see Listing~\ref{lst:Matlab_code_example}
```

This template has support for Matlab, C++ and Verilog code.
