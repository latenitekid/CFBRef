import logging.handlers

import wiki
import utils
import globals
from globals import actions

log = logging.getLogger("bot")


def setStateTouchback(game, isHome):
	game['status']['location'] = 25
	game['status']['down'] = 1
	game['status']['yards'] = 10
	game['status']['possession'] = utils.getHomeAwayString(isHome)
	game['waitingAction'] = actions.play
	game['waitingOn'] = utils.reverseHomeAway(utils.getHomeAwayString(isHome))


def findNumberInRangeDict(number, dict):
	for key in dict:
		rangeStart, rangeEnd = utils.getRange(key)
		if rangeStart is None:
			log.warning("Could not extract range: {}".format(key))
			continue

		if rangeStart <= number <= rangeEnd:
			return dict[key]

	log.warning("Could not find number in dict")
	return None


def getPlayResult(game, play, number):
	playDict = wiki.getPlay(play)
	if playDict is None:
		log.warning("{} is not a valid play".format(play))
		return None

	if play in globals.movementPlays:
		offense = game[game['status']['possession']]['offense']
		defense = game[utils.reverseHomeAway(game['status']['possession'])]['defense']
		playMajorRange = playDict[offense][defense]
	else:
		playMajorRange = playDict

	playMinorRange = findNumberInRangeDict(game['status']['location'], playMajorRange)
	return findNumberInRangeDict(number, playMinorRange)


def transform(game, play, number):
	return ""


def executePlay(game):
	return ""
