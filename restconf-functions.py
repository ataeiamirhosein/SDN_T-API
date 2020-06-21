"""The ADVA/PoliMi RESTCONF SDN course functions."""

from logging import Logger, getLogger

import requests

from policonf.magic import course_function


#: The Python ``Logger`` instance for mod:`policonf`.
LOG: Logger = getLogger(__package__)


@course_function(shortcut="t")
def get_context():
    """Get full TAPI context."""
    LOG.info("Getting full TAPI context...")

    # If you want to implement this PoliMi SDN course function, then just
    # remove the following lines and start coding...
    raise NotImplementedError(
        "This ADVA/PoliMi SDN course function needs your implementation :)")


@course_function(shortcut="p")
def get_sips():
    """Get service interface points from TAPI."""
    LOG.info("Getting service interface points from TAPI...")

    # If you want to implement this PoliMi SDN course function, then just
    # remove the following lines and start coding...
    raise NotImplementedError(
        "This ADVA/PoliMi SDN course function needs your implementation :)")


@course_function(shortcut="u")
def get_topology_uuids():
    """Get topology UUIDs from TAPI."""
    LOG.info("Getting topology UUIDs from TAPI...")

    # If you want to implement this PoliMi SDN course function, then just
    # remove the following lines and start coding...
    raise NotImplementedError(
        "This ADVA/PoliMi SDN course function needs your implementation :)")


@course_function(shortcut="n")
def get_node_uuids():
    """Get node UUIDs from TAPI."""
    LOG.info("Getting node UUIDs from TAPI...")

    # If you want to implement this PoliMi SDN course function, then just
    # remove the following lines and start coding...
    raise NotImplementedError(
        "This ADVA/PoliMi SDN course function needs your implementation :)")


@course_function(shortcut="l")
def get_link_uuids():
    """Get link UUIDs from TAPI."""
    LOG.info("Getting link UUIDs from TAPI...")

    # If you want to implement this PoliMi SDN course function, then just
    # remove the following lines and start coding...
    raise NotImplementedError(
        "This ADVA/PoliMi SDN course function needs your implementation :)")


@course_function(shortcut="c")
def get_connection_uuids():
    """Get connection UUIDs from TAPI."""
    LOG.info("Getting connection UUIDs from TAPI...")

    # If you want to implement this PoliMi SDN course function, then just
    # remove the following lines and start coding...
    raise NotImplementedError(
        "This ADVA/PoliMi SDN course function needs your implementation :)")


@course_function(shortcut="s")
def create_connectivity_service():
    """Create a new TAPI connectivity service."""
    LOG.info("Creating TAPI connectivity service...")

    # If you want to implement this PoliMi SDN course function, then just
    # remove the following lines and start coding...
    raise NotImplementedError(
        "This ADVA/PoliMi SDN course function needs your implementation :)")
