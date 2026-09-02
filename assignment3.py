"""Functions for PGE 323M Assignment 3."""

import yaml


def water_rel_perm(krw_o, Sor, Swc, nw):
    """Return modified Brooks-Corey water relative permeability at three saturations."""
    raise NotImplementedError("Complete water_rel_perm")


def read_well_activity(filename):
    """Return nonblank well-activity records as lists of stripped strings."""
    with open(filename, encoding="utf-8") as stream:
        return [
            [field.strip() for field in line.split(",")]
            for line in stream
            if line.strip()
        ]


def add_well_activity(well_list, new_well_name, activity, days):
    """Append a well activity, sort the list numerically by day, and return it."""
    raise NotImplementedError("Complete add_well_activity")


def add_well_activity_from_file(filename, new_well_name, activity, days):
    """Read well activities, add one record, and return the sorted list."""
    raise NotImplementedError("Complete add_well_activity_from_file")


def read_well_parameters(filename):
    """Safely load and return well parameters from a YAML file."""
    with open(filename, encoding="utf-8") as stream:
        return yaml.safe_load(stream)


def get_bhp_well_values(well_parameter_dict):
    """Return the values associated with bottom-hole-pressure well controls."""
    raise NotImplementedError("Complete get_bhp_well_values")


def get_bhp_well_values_from_file(filename):
    """Load a well-parameter file and return its BHP well-control values."""
    raise NotImplementedError("Complete get_bhp_well_values_from_file")
