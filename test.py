#!/usr/bin/env python

from dbc import *

print ChatProfanityDBC('ChatProfanity.dbc').read()[0]
print GameTipsDBC('GameTips.dbc').read()[0]
print SpamMessagesDBC('SpamMessages.dbc').read()[0]
print AchievementDBC('Achievement.dbc').read()[0]
print AchievementCategoryDBC('Achievement_Category.dbc').read()[0]
print AchievementCriteriaDBC('Achievement_Criteria.dbc').read()[0]