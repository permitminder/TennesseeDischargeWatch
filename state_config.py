"""
State configuration for this TennesseeDischargeWatch instance.

All state-specific values are centralized here. To deploy for a new state,
run: python deploy_new_state.py <STATE_CODE>

This file is overwritten by deploy_new_state.py — do not add logic here.
"""

STATE_CODE = "TN"
STATE_NAME = "Tennessee"
APP_NAME = "TennesseeDischargeWatch"
APP_TAGLINE = "Tennessee Discharge Monitoring"
DOMAIN = "tennesseedischargewatch.org"
DATA_FILE = "tn_exceedances_launch_ready.csv"
CONTACT_EMAIL = "data@tennesseedischargewatch.org"
MAILING_ADDRESS = ""
TIMEZONE_LABEL = "CST"
EPA_REGION = 4
