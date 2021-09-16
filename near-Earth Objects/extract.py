"""Extract data on near-Earth objects and close approaches from CSV and JSON
files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the
command line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json
import os


from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about
                         near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """

    neoCollection = []
    with open(neo_csv_path, 'r') as file:
        csvData = csv.DictReader(file)
        for element in csvData:
            neoCollection.append(NearEarthObject(**element))

    return neoCollection


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about
                        close approaches.
    :return: A collection of `CloseApproach`es.
    """
    approachCollection = []
    with open(cad_json_path, 'r') as file:
        jsonData = json.load(file)
        cadData = jsonData['data']

        for approach in cadData:
            approachCollection.append(CloseApproach(*approach))

    return approachCollection
