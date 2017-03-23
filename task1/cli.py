import click
import task1

HELP = {
    'form': 'Form ID to get responses for. Defaults to the first form in the list of all forms.',
    'apikey': 'API key. Required',
    'output': 'Path to output file. Prints to stdout if not specified.'
}


@click.command()
@click.option('-f', '--form', default=None, help=HELP['form'])
@click.option('-k', '--apikey', required=True, help=HELP['apikey'])
@click.option('-o', '--output', default=None, help=HELP['output'])
def run(form, apikey, output):
    """Generate a CSV with all the responses for a given form."""
    csv = task1.get_responses_csv(form_id=form, apikey=apikey)

    if output:
        with open(output, 'w') as f:
            f.write(csv)
    else:
        print(csv)


if __name__ == '__main__':
    run()
