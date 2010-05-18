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
    
class CharTitlesDBC(DBCFile):
    skeleton = [
        Int32('ID'),
        Int32('Unknown'),
        Localization('TitleMale'),
        Localization('TitleFemale'),
        Int32('SelectionIndex'),
    ]

class SpellDBC(DBCFile):
    skeleton = [
        UInt32('ID'),
        UInt32('Category'),
        UInt32('Dispel'),
        UInt32('Mechanic'),
        UInt32('Attributes'),
        Array('AttributesEx', UInt32, 6), 
        UInt32('Unk1'),
        UInt32('Stances'),
        UInt32('Unk2'),
        UInt32('StancesNot'),
        UInt32('Unk3'),
        UInt32('Targets'),
        UInt32('TargetCreatureType'),
        UInt32('RequiresSpellFocus'),
        UInt32('FacingCasterFlags'),
        UInt32('CasterAuraState'),
        UInt32('TargetAuraState'),
        UInt32('CasterAuraStateNot'),
        UInt32('TargetAuraStateNot'),
        UInt32('CasterAuraSpell'),
        UInt32('TargetAuraSpell'),
        UInt32('ExcludeCasterAuraSpell'),
        UInt32('ExcludeTargetAuraSpell'),
        UInt32('CastingTimeIndex'),
        UInt32('RecoveryTime'),
        UInt32('CategoryRecoveryTime'),
        UInt32('InterruptFlags'),
        UInt32('AuraInterruptFlags'),
        UInt32('ChannelInterruptFlags'),
        UInt32('ProcFlags'),
        UInt32('ProcChance'),
        UInt32('ProcCharges'),
        UInt32('MaxLevel'),
        UInt32('BaseLevel'),
        UInt32('SpellLevel'),
        UInt32('DurationIndex'),
        UInt32('PowerType'),
        UInt32('ManaCost'),
        UInt32('ManaCostPerLevel'),
        UInt32('ManaPerSecond'),
        UInt32('ManaPerSecondPerLevel'),
        UInt32('RangeIndex'),
        Float('Speed'),
        UInt32('ModalNextSpell'),
        UInt32('StackAmount'),
        Array('Totem', UInt32, 2),
        Array('Reagent', Int32, 8),
        Array('ReagentCount', UInt32, 8),
        Int32('EquippedItemClass'),
        Int32('EquippedItemSubClassMask'),
        Int32('EquippedItemInventoryTypeMask'),
        Array('Effect', Int32, 3),
        Array('EffectDieSides', Int32, 3),
        Array('EffectRealPointsPerLevel', Int32, 3),
        Array('EffectBasePoints', Int32, 3),
        Array('EffectMechanic', UInt32, 3),
        Array('EffectImplicitTargetA', UInt32, 3),
        Array('EffectImplicitTargetB', UInt32, 3),
        Array('EffectRadiusIndex', UInt32, 3),
        Array('EffectApplyAuraName', UInt32, 3),
        Array('EffectAmplitude', UInt32, 3),
        Array('EffectMultipleValue', Float, 3),
        Array('EffectChainTarget', UInt32, 3),
        Array('EffectItemType', UInt32, 3),
        Array('EffectMiscValue', Int32, 3),
        Array('EffectMiscValueB', Int32, 3),
        Array('EffectTriggerSpell', UInt32, 3),
        Array('EffectPointsPerComboPoint', Float, 3),
        Array('EffectSpellClassMaskA', UInt32, 3),
        Array('EffectSpellClassMaskB', UInt32, 3),
        Array('EffectSpellClassMaskC', UInt32, 3),
        Array('SpellVisual', UInt32, 2),
        UInt32('SpellIconID'),
        UInt32('ActiveIconID'),
        UInt32('SpellPriority'),
        Localization('SpellName'),
        Localization('Rank'),
        Localization('Description'),
        Localization('ToolTip'),
        UInt32('ManaCostPercentage'),
        UInt32('StartRecoveryCategory'),
        UInt32('StartRecoveryTime'),
        UInt32('MaxTargetLevel'),
        UInt32('SpellFamilyName'),
        UInt64('SpellFamilyFlags'),
        UInt32('SpellFamilyFlags2'),
        UInt32('MaxAffectedTargets'),
        UInt32('DmgClass'),
        UInt32('PreventionType'),
        UInt32('StanceOrderBar'),
        Array('DmgMultiplier', Float, 3),
        UInt32('MinFactionID'),
        UInt32('MinReputation'),
        UInt32('RequiredAuraVision'),
        Array('TotemCategory', UInt32, 2),
        Int32('AreaGroupID'),
        UInt32('SchoolMask'),
        UInt32('RuneCostID'),
        UInt32('SpellMissileID'),
        UInt32('PowerDisplayID'),
        Array('Unk4', Float, 3),
        UInt32('SpellDescriptionVariableID'),
        UInt32('SpellDifficultyID'),
    ]