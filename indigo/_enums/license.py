
import enum


class kLicenseStatus(enum.Enum):
    Unknown = 0
    """Unknown license status."""

    ActiveTrial = 1
    """The license is a trial"""

    ActiveSubscription = 2
    """The license has a valid Indigo Up-to-Date subscription with access to the reflector."""

    ExpiredSubscription = 3
    """The license has an expired Indigo Up-to-Date subscription. No access to the reflector."""
