PY_M='python3 -m '
PIP=${PY_M}poetry


#NAME=realpython-reader-wip
#NAME=reader-pn
NAME=mypkg-wip
REPO=https://github.com/uncsco/RealPython_reader.git

BRANCH=pn-wip
#HASH=6a2a8fce54aa8ae72c62c5aca3618ac059d5d4bf
#HASH=1984b638d37378ddb4d2095c44b9dfdf3124e24a
#HASH=e59cae1b39572465c7c562a97baa74fafabed5c5
#// ONLY one is NON-blank
_REV=@${BRANCH}${HASH}

#// TODO: [rich,excel]
EXTRAS=rich,excel
_EXTRAS_=[${EXTRAS}]


## pip - OKAY
#############
#PIP=${PY_M}pip

#$PIP install --upgrade git+${REPO}@${BRANCH}
#?? `--install-option`: https://stackoverflow.com/questions/52717761/how-can-i-install-extras-with-pip-install-gitssh
#$PIP install --install-option="--extras-require=${EXTRAS}" git+${REPO}${_REV}

#// `#egg=...[...]`: https://stackoverflow.com/q/30239152
###################
#$PIP install git+${REPO}${_REV}#egg=${NAME}${_EXTRAS_}
#             git+https://github.com/uncsco/RealPython_reader.git@pn-wip#egg=mypkg-wip
#                                                                 ====== =============

#$PIP uninstall $NAME



## POETRY
#########

# $PIP remove numpy

# $PIP add --dev pipdeptree
#$PY_M pipdeptree


#// ADD...
#$PIP add git+${REPO}@${HASH} # ALT
#$PIP add git+${REPO}@${BRANCH}${_EXTRAS_}
#$PIP add git+${REPO}${_REV}${_EXTRAS_}

#// UPDATE... // NOTE: Need to update `version` in setup.py
#$PIP update $NAME

#// REMOVE...
#$PIP remove $NAME
