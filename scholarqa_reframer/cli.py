"""
Command-line interface for the ScholarQA Mechanistic Query Reframer.
"""

import sys
import json
import click
from .engine import MechanisticReframer


@click.command()
@click.argument("query", required=False)
@click.option("--json-output", is_flag=True, help="Output raw JSON instead of formatted text.")
@click.option("--sample", type=int, default=0, help="Run on sample benchmark query (1=thermal velocity, 2=acoustic impedance, 3=membrane).")
def main(query: str, json_output: bool, sample: int):
    """Reframes a raw scientific question into a multi-dimensional ScholarQA open inquiry."""
    
    samples = {
        1: "Does solvent viscosity damp bacterial instantaneous thermal velocity according to Stokes' drag?",
        2: "Does characteristic sound speed determine the acoustic boundary reflection coefficient?",
        3: "Does passive diffusion of small molecules across a lipid bilayer require ATP transport?",
    }

    if sample in samples:
        query = samples[sample]

    if not query:
        click.echo("Error: Please provide a query string or specify --sample [1, 2, 3].", err=True)
        sys.exit(1)

    reframer = MechanisticReframer()
    reframed = reframer.reframe(query)

    if json_output:
        click.echo(reframed.model_dump_json(indent=2))
        return

    # Formatted Terminal Output
    click.echo("\n" + "=" * 76)
    click.echo(" 🔬 SCHOLARQA MECHANISTIC QUERY REFRAMER")
    click.echo("=" * 76)
    
    click.echo("\n[1] YOUR RAW INQUIRY / HYPOTHESIS:")
    click.secho(f"    \"{reframed.original_query}\"", fg="yellow")

    click.echo("\n[2] SCHOLARQA MECHANISTIC REFRAMING (THE 'BETTER WAY'):")
    click.secho(f"    \"{reframed.scholarqa_mechanistic_query}\"", fg="green", bold=True)

    click.echo("\n[3] CORE GOVERNING PRINCIPLE:")
    click.secho(f"    {reframed.core_governing_principle}", fg="cyan")

    click.echo("\n[4] DECOUPLED PHYSICAL DIMENSIONS:")
    for dim in reframed.decoupled_dimensions:
        click.echo(f"    • {dim.dimension_name}:")
        click.echo(f"        Conflated: {dim.conflated_role}")
        click.secho(f"        Rigorous:  {dim.rigorous_role}", fg="white")
        click.secho(f"        Equation:  {dim.governing_equation_or_rule}", fg="cyan")

    click.echo("\n[5] BOUNDARY REGIMES & ASSUMPTIONS:")
    for b in reframed.boundary_regimes:
        click.echo(f"    • {b}")

    click.echo("\n[6] HIGH-SIGNAL RETRIEVAL PROBES (Target Literature on Disk):")
    for probe in reframed.retrieval_probes:
        click.secho(f"    • [{probe.probe_name}]", fg="magenta")
        click.echo(f"        Keywords: {probe.search_keywords}")
        click.echo(f"        Anchor:   {probe.target_corpus_anchor}")

    click.echo("\n[7] PEDAGOGICAL CRITIQUE (Why this reframing is superior):")
    click.echo(f"    {reframed.pedagogical_critique}")

    click.echo("\n[8] PREVENTED AI FAILURE MODE:")
    click.secho(f"    🛡️  {reframed.avoided_failure_mode}", fg="bright_green")
    click.echo("=" * 76 + "\n")


if __name__ == "__main__":
    main()
