#!/usr/bin/env python

from dbcfile import DBCFile
from dtypes import *

class ChatProfanityDBC(DBCFile):
    "A collection of all the words censored by the word filter (as a regex)"
    skeleton = [
        Int32('id'),
        String('word'),
        Int32('lang'),
    ]
    
class GameTipsDBC(DBCFile):
    "A collection of tips displayed during loading screens"
    skeleton = [
        Int32('ID'),
        Localization('Tip'),
    ]

class SpamMessagesDBC(DBCFile):
    "A collection of Regular Expressions to match spam websites"
    skeleton = [
        Int32('ID'),
        String('RegEx'),
    ]

class AchievementDBC(DBCFile):
    skeleton = [
        Int32('ID'),
        Int32('Faction'),
        Int32('Map'),
        Int32('Parent'),
        Localization('Name'),
        Localization('Description'),
        Int32('Category'),
        Int32('Points'),
        Int32('SortOrder'),
        UInt32('Flags'),
        Int32('Icon'),
        Localization('TitleReward'),
        Int32('Count'),
        Int32('RefAchievement'),
    ]

class AchievementCategoryDBC(DBCFile):
    "Achievement Categories"
    skeleton = [
        Int32('ID'),
        Int32('Parent'),
        Localization('Name'),
        UInt32('SortOrder'),
    ]

class AchievementCriteriaDBC(DBCFile):
    skeleton = [
        Int32('ID'),
        Int32('AchievementID'),
        Int32('Type'),
        Array('Values', Int32, 6),
        Localization('Description'),
        Int32('CompletionFlag'),
        Int32('GroupFlag'),
        Int32('TimedID'),
        Int32('TimeLimit'),
        Int32('SortOrder'),
    ]