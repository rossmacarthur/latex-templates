#!/usr/bin/python

import click
import re

RSTCLR = '\033[0m'
FDDCLR = '\033[90m'


def index_entries(text):
    """
    Construct a dictionary of entries from 'text'.
    """
    p = re.compile('(?<=\\\\nomenclature{).*}.*{.*(?=})')
    return {x.split('}{')[0]: x.split('}{')[1] for x in p.findall(text)}


def find_acronyms(text):
    """
    Find all acronyms in 'text'.
    """
    p = re.compile('\\b[A-Z][A-Za-z0-9]*[A-Z]\\b')
    return list(sorted(set(p.findall(text))))


def get_context(text, acronym):
    """
    Print out the first use context of the acronym in given text.
    """
    p = re.compile('\\b{}\\b'.format(acronym))
    x = p.search(text).start()
    text = text.replace('\n', ' ').replace(acronym, RSTCLR+acronym+FDDCLR)
    return '\n' + FDDCLR + '...' + text[max(0, x-25):x+50] + '...' + RSTCLR


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.argument('body', nargs=-1, type=click.Path(exists=True))
@click.option('--nom-path', '-f', type=click.Path(exists=True),
              help='File containing LaTeX nomenclature entries')
@click.option('--prompts', '-p', is_flag=True,
              help='Prompt to enter missing entries.')
@click.option('--output', '-o', is_flag=True,
              help='Write code to nomenclature file.')
def main(body, nom_path, prompts, output):
    """
    Script interface for updating LaTeX nomenclature entries.

    BODY is the file(s) containing the acronyms (e.g. body.tex or *.tex).
    All acronyms found will be printed out. The optional argument '--prompts'
    allows you to enter the descriptions for the acronyms, after which LaTeX
    nomenclature code will be outputted. Optionally, this code can also be
    output to a file.
    """
    body_text = ''.join(open(file, 'r').read() for file in body)
    acronyms = find_acronyms(body_text)
    entries = index_entries(open(nom_path, 'r').read() if nom_path else '')

    if nom_path:
        click.echo('Entries in given file:')
        for e in sorted(entries):
            click.echo('{}\t\t{}'.format(e, entries[e]))
        click.echo()

    if prompts:
        click.echo('New acronyms:')
        for a in sorted(set(acronyms)-set(entries.keys())):
            click.echo(get_context(body_text, a))
            desc = click.prompt('Enter a description for ' + a,
                                default='blank to skip')
            if desc != 'blank to skip':
                entries[a] = desc

        if entries:
            nom_code = ['\\nomenclature{{{}}}{{{}}}\n'.format(k, v)
                        for k, v in sorted(entries.items())]
            click.echo('\nLaTeX code:' + FDDCLR)
            click.echo(''.join(nom_code) + RSTCLR)

            if output:
                if nom_path:
                    nom_file = open(nom_path, 'w')
                else:
                    file = click.prompt('Please specify an output file',
                                        type=click.Path())
                    nom_file = open(file, 'w')
                click.echo('\\makenomenclature\n', file=nom_file)
                click.echo(''.join(nom_code), file=nom_file)
                click.echo('\\printnomenclature', file=nom_file)
                click.echo('LaTeX code written to file.')
    elif set(acronyms)-set(entries.keys()):
        click.echo('New acronyms:')
        for a in sorted(set(acronyms)-set(entries.keys())):
            click.echo(a)
    elif acronyms:
        click.echo('No new acronyms.')
    else:
        click.echo('No acronyms.')


if __name__ == '__main__':
    main()
