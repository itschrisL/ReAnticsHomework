# -*- coding: latin-1 -*-
import random
import sys
if 64 - 64: i11iIiiIii
sys . path . append ( ".." )
from Player import *
from Constants import *
from Construction import CONSTR_STATS
from Ant import UNIT_STATS
from Move import Move
from GameState import addCoords
from AIPlayerUtils import *
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
if 73 - 73: II111iiii
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
if 48 - 48: iII111i % IiII + I1Ii111 / ooOoO0o * Ii1I
if 46 - 46: ooOoO0o * I11i - OoooooooOO
if 30 - 30: o0oOOo0O0Ooo - O0 % o0oOOo0O0Ooo - OoooooooOO * O0 * OoooooooOO
if 60 - 60: iIii1I11I1II1 / i1IIi * oO0o - I1ii11iIi11i + o0oOOo0O0Ooo
if 94 - 94: i1IIi % Oo0Ooo
if 68 - 68: Ii1I / O0
class Iiii111Ii11I1 ( ) :
 def __init__ ( self , foodCoords , depositCoords ) :
  self . antList = [ ]
  self . food = foodCoords
  self . deposit = depositCoords
  self . dist = approxDist ( foodCoords , depositCoords )
  self . state = None
  if 66 - 66: iII111i
  if 30 - 30: iIii1I11I1II1 * iIii1I11I1II1 . II111iiii - oO0o
 def addAnt ( self , newCoords ) :
  self . antList . append ( newCoords )
  if 72 - 72: II111iiii - OoOoOO00
  if 91 - 91: OoO0O00 . i11iIiiIii / oO0o % I11i / OoO0O00 - i11iIiiIii
  if 8 - 8: o0oOOo0O0Ooo * I1ii11iIi11i * iIii1I11I1II1 . IiII / IiII % IiII
 def updateNextAnt ( self ) :
  for i11 in self . antList :
   I11 = getAntAt ( self . state , i11 )
   if I11 is not None :
    if not I11 . hasMoved :
     if I11 . carrying :
      Oo0o0000o0o0 = createPathToward ( self . state , i11 , self . deposit , UNIT_STATS [ WORKER ] [ MOVEMENT ] )
      self . antList . append ( Oo0o0000o0o0 [ len ( Oo0o0000o0o0 ) - 1 ] )
      return Move ( MOVE_ANT , Oo0o0000o0o0 , None )
     else :
      Oo0o0000o0o0 = createPathToward ( self . state , i11 , self . food , UNIT_STATS [ WORKER ] [ MOVEMENT ] )
      self . antList . append ( Oo0o0000o0o0 [ len ( Oo0o0000o0o0 ) - 1 ] )
      return Move ( MOVE_ANT , Oo0o0000o0o0 , None )
  return None
  if 86 - 86: OoOoOO00 % I1IiiI
  if 80 - 80: OoooooooOO . I1IiiI
 def updateState ( self , newState ) :
  self . state = newState
  if 87 - 87: oO0o / ooOoO0o + I1Ii111 - ooOoO0o . ooOoO0o / II111iiii
  iiIIIIi1i1 = [ ]
  for i11 in self . antList :
   O0OoOoo00o = getAntAt ( self . state , i11 )
   if O0OoOoo00o is None or O0OoOoo00o . player != self . state . whoseTurn or O0OoOoo00o . type != WORKER :
    iiIIIIi1i1 . append ( i11 )
    if 31 - 31: II111iiii + OoO0O00 . I1Ii111
  for i11 in iiIIIIi1i1 :
   self . antList . remove ( i11 )
   if 68 - 68: I1IiiI - i11iIiiIii - OoO0O00 / OOooOOo - OoO0O00 + i1IIi
   if 48 - 48: OoooooooOO % o0oOOo0O0Ooo . I1IiiI - Ii1I % i1IIi % OoooooooOO
   if 3 - 3: iII111i + O0
   if 42 - 42: OOooOOo / i1IIi + i11iIiiIii - Ii1I
   if 78 - 78: OoO0O00
   if 18 - 18: O0 - iII111i / iII111i + ooOoO0o % ooOoO0o - IiII
   if 62 - 62: iII111i - IiII - OoOoOO00 % i1IIi / oO0o
   if 77 - 77: II111iiii - II111iiii . I1IiiI / o0oOOo0O0Ooo
   if 14 - 14: I11i % O0
   if 41 - 41: i1IIi + I1Ii111 + OOooOOo - IiII
   if 77 - 77: Oo0Ooo . IiII % ooOoO0o
class AIPlayer ( Player ) :
 if 41 - 41: OoOoOO00
 if 13 - 13: Oo0Ooo . i11iIiiIii - iIii1I11I1II1 - OoOoOO00
 if 6 - 6: I1IiiI / Oo0Ooo % Ii1I
 if 84 - 84: i11iIiiIii . o0oOOo0O0Ooo
 if 100 - 100: Ii1I - Ii1I - I1Ii111
 if 20 - 20: OoooooooOO
 if 13 - 13: i1IIi - Ii1I % oO0o / iIii1I11I1II1 % iII111i
 def __init__ ( self , inputPlayerId ) :
  super ( AIPlayer , self ) . __init__ ( inputPlayerId , "Hard to Beat" )
  self . foods = None
  self . distances = [ 0 for oo in range ( 2 ) ]
  self . hill = None
  self . tunnel = None
  self . paths = None
  self . CurDecision = - 1
  if 68 - 68: I11i + OOooOOo . iIii1I11I1II1 - IiII % iIii1I11I1II1 - ooOoO0o
  if 79 - 79: Oo0Ooo + I1IiiI - iII111i
  if 83 - 83: ooOoO0o
  self . o_food = [ ]
  self . occupants = [ None , None ]
  if 64 - 64: OoO0O00 % ooOoO0o % iII111i / OoOoOO00 - OoO0O00
  if 74 - 74: iII111i * O0
  if 89 - 89: oO0o + Oo0Ooo
  if 3 - 3: i1IIi / I1IiiI % I11i * i11iIiiIii / O0 * I11i
  if 49 - 49: oO0o % Ii1I + i1IIi . I1IiiI % I1ii11iIi11i
  if 48 - 48: I11i + I11i / II111iiii / iIii1I11I1II1
  if 20 - 20: o0oOOo0O0Ooo
  if 77 - 77: OoOoOO00 / I11i
  if 98 - 98: iIii1I11I1II1 / i1IIi / i11iIiiIii / o0oOOo0O0Ooo
  if 28 - 28: OOooOOo - IiII . IiII + OoOoOO00 - OoooooooOO + O0
  if 95 - 95: OoO0O00 % oO0o . O0
  if 15 - 15: ooOoO0o / Ii1I . Ii1I - i1IIi
  if 53 - 53: IiII + I1IiiI * oO0o
  if 61 - 61: i1IIi * OOooOOo / OoooooooOO . i11iIiiIii . OoOoOO00
  if 60 - 60: I11i / I11i
  if 46 - 46: Ii1I * OOooOOo - OoO0O00 * oO0o - I1Ii111
  if 83 - 83: OoooooooOO
  if 31 - 31: II111iiii - OOooOOo . I1Ii111 % OoOoOO00 - O0
  if 4 - 4: II111iiii / ooOoO0o . iII111i
  if 58 - 58: OOooOOo * i11iIiiIii / OoOoOO00 % I1Ii111 - I1ii11iIi11i / oO0o
  if 50 - 50: I1IiiI
  if 34 - 34: I1IiiI * II111iiii % iII111i * OoOoOO00 - I1IiiI
  if 33 - 33: o0oOOo0O0Ooo + OOooOOo * OoO0O00 - Oo0Ooo / oO0o % Ii1I
  if 21 - 21: OoO0O00 * iIii1I11I1II1 % oO0o * i1IIi
 def getPlacement ( self , currentState ) :
  if currentState . phase == SETUP_PHASE_1 :
   if 16 - 16: O0 - I1Ii111 * iIii1I11I1II1 + iII111i
   self . foods = None
   self . distances = [ 0 for oo in range ( 2 ) ]
   self . hill = None
   self . tunnel = None
   self . paths = None
   if 50 - 50: II111iiii - ooOoO0o * I1ii11iIi11i / I1Ii111 + o0oOOo0O0Ooo
   if 88 - 88: Ii1I / I1Ii111 + iII111i - II111iiii / ooOoO0o - OoOoOO00
   return [ ( 2 , 1 ) , ( 7 , 2 ) ,
 ( 0 , 3 ) , ( 1 , 3 ) , ( 2 , 3 ) , ( 3 , 3 ) , ( 4 , 3 ) , ( 6 , 3 ) , ( 7 , 3 ) , ( 8 , 3 ) , ( 9 , 3 ) ]
  elif currentState . phase == SETUP_PHASE_2 :
   IIIIii = 2
   self . o_food = [ ]
   if 70 - 70: Ii1I / I11i . iII111i % Oo0Ooo
   OOoOO00OOO0OO = 1 - currentState . whoseTurn
   iI1I111Ii111i = getConstrList ( currentState , OOoOO00OOO0OO , ( ANTHILL , ) ) [ 0 ]
   I11IiI1I11i1i = getConstrList ( currentState , OOoOO00OOO0OO , ( TUNNEL , ) ) [ 0 ]
   if 38 - 38: o0oOOo0O0Ooo
   if 57 - 57: O0 / oO0o * I1Ii111 / OoOoOO00 . II111iiii
   for oo in range ( 0 , IIIIii ) :
    i11iIIIIIi1 = None
    iiII1i1 = 0
    for o00oOO0o in range ( 10 ) :
     for OOO00O in range ( 6 , 10 ) :
      if getConstrAt ( currentState , ( o00oOO0o , OOO00O ) ) is None :
       OOoOO0oo0ooO = stepsToReach ( currentState , ( o00oOO0o , OOO00O ) , iI1I111Ii111i . coords )
       O0o0O00Oo0o0 = stepsToReach ( currentState , ( o00oOO0o , OOO00O ) , I11IiI1I11i1i . coords )
       if 87 - 87: ooOoO0o * Oo0Ooo % i11iIiiIii % OoOoOO00 - OOooOOo
       if min ( OOoOO0oo0ooO , O0o0O00Oo0o0 ) > iiII1i1 and oo == 0 :
        iiII1i1 = min ( OOoOO0oo0ooO , O0o0O00Oo0o0 )
        i11iIIIIIi1 = ( o00oOO0o , OOO00O )
        if 68 - 68: I1Ii111 % i1IIi . IiII . I1ii11iIi11i
       if min ( OOoOO0oo0ooO , O0o0O00Oo0o0 ) > iiII1i1 and oo == 1 :
        if not self . o_food [ 0 ] == ( o00oOO0o , OOO00O ) :
         iiII1i1 = min ( OOoOO0oo0ooO , O0o0O00Oo0o0 )
         i11iIIIIIi1 = ( o00oOO0o , OOO00O )
    self . o_food . append ( i11iIIIIIi1 )
    if 92 - 92: iII111i . I1Ii111
   return self . o_food
  else :
   return None
   if 31 - 31: I1Ii111 . OoOoOO00 / O0
   if 89 - 89: OoOoOO00
   if 68 - 68: OoO0O00 * OoooooooOO % O0 + OoO0O00 + ooOoO0o
   if 4 - 4: ooOoO0o + O0 * OOooOOo
   if 55 - 55: Oo0Ooo + iIii1I11I1II1 / OoOoOO00 * oO0o - i11iIiiIii - Ii1I
   if 25 - 25: I1ii11iIi11i
   if 7 - 7: i1IIi / I1IiiI * I1Ii111 . IiII . iIii1I11I1II1
   if 13 - 13: OOooOOo / i11iIiiIii
   if 2 - 2: I1IiiI / O0 / o0oOOo0O0Ooo % OoOoOO00 % Ii1I
   if 52 - 52: o0oOOo0O0Ooo
   if 95 - 95: Ii1I
   if 87 - 87: ooOoO0o + OoOoOO00 . OOooOOo + OoOoOO00
   if 91 - 91: O0
   if 61 - 61: II111iiii
   if 64 - 64: ooOoO0o / OoOoOO00 - O0 - I11i
   if 86 - 86: I11i % OoOoOO00 / I1IiiI / OoOoOO00
   if 42 - 42: OoO0O00
   if 67 - 67: I1Ii111 . iII111i . O0
   if 10 - 10: I1ii11iIi11i % I1ii11iIi11i - iIii1I11I1II1 / OOooOOo + Ii1I
   if 87 - 87: oO0o * I1ii11iIi11i + OOooOOo / iIii1I11I1II1 / iII111i
   if 37 - 37: iII111i - ooOoO0o * oO0o % i11iIiiIii - I1Ii111
 def getMove ( self , currentState ) :
  if 83 - 83: I11i / I1IiiI
  iIIiIi1iIII1 = getCurrPlayerInventory ( currentState )
  Ooo = currentState . whoseTurn
  OOoOO00OOO0OO = 1 - currentState . whoseTurn
  if 62 - 62: OOooOOo / OoO0O00 + Ii1I / OoO0O00 . II111iiii
  if 68 - 68: i11iIiiIii % I1ii11iIi11i + i11iIiiIii
  iii = getAntList ( currentState , OOoOO00OOO0OO , ( WORKER , ) )
  II1I = len ( iii )
  if 84 - 84: IiII . i11iIiiIii . IiII * I1ii11iIi11i - I11i
  if 42 - 42: i11iIiiIii
  I11i1iIII = getAntList ( currentState , OOoOO00OOO0OO , ( DRONE , ) )
  iiIiI = getAntList ( currentState , OOoOO00OOO0OO , ( R_SOLDIER , ) )
  o00oooO0Oo = getAntList ( currentState , OOoOO00OOO0OO , ( SOLDIER , ) )
  if 78 - 78: Ii1I % I1Ii111 + I1ii11iIi11i
  if 64 - 64: oO0o * O0 . I1IiiI + II111iiii
  if self . hill is None :
   self . hill = getConstrList ( currentState , Ooo , ( ANTHILL , ) ) [ 0 ]
  if self . tunnel is None :
   self . tunnel = getConstrList ( currentState , Ooo , ( TUNNEL , ) ) [ 0 ]
   if 6 - 6: OoOoOO00 / iII111i . IiII . IiII
   if 62 - 62: I1ii11iIi11i + IiII % iII111i + OOooOOo
  if self . paths is None :
   if 33 - 33: O0 . IiII . I1IiiI
   self . paths = [ 0 for oo in range ( 2 ) ]
   if 72 - 72: i1IIi / OoO0O00 + OoooooooOO - Oo0Ooo
   iI1Iii = getConstrList ( currentState , None , ( FOOD , ) )
   oO00OOoO00 = 999
   IiI111111IIII = None
   for i1Ii in iI1Iii :
    ii111iI1iIi1 = stepsToReach ( currentState , self . tunnel . coords , i1Ii . coords )
    if ii111iI1iIi1 < oO00OOoO00 :
     oO00OOoO00 = ii111iI1iIi1
     IiI111111IIII = i1Ii . coords
     if 78 - 78: OoO0O00 . OOooOOo + OoO0O00 / I11i / OoO0O00
   oO00OOoO00 = 999
   oO0O00OoOO0 = None
   for i1Ii in iI1Iii :
    ii111iI1iIi1 = stepsToReach ( currentState , self . hill . coords , i1Ii . coords )
    if ii111iI1iIi1 < oO00OOoO00 :
     oO00OOoO00 = ii111iI1iIi1
     oO0O00OoOO0 = i1Ii . coords
     if 82 - 82: II111iiii . IiII - iIii1I11I1II1 - IiII * II111iiii
   if IiI111111IIII == oO0O00OoOO0 :
    oO00OOoO00 = 999
    for i1Ii in iI1Iii :
     ii111iI1iIi1 = stepsToReach ( currentState , self . hill . coords , i1Ii . coords )
     if ii111iI1iIi1 < oO00OOoO00 :
      if i1Ii . coords != IiI111111IIII :
       oO00OOoO00 = ii111iI1iIi1
       oO0O00OoOO0 = i1Ii . coords
       if 77 - 77: iIii1I11I1II1 * OoO0O00
   self . paths [ 0 ] = Iiii111Ii11I1 ( oO0O00OoOO0 , self . hill . coords )
   self . paths [ 1 ] = Iiii111Ii11I1 ( IiI111111IIII , self . tunnel . coords )
   if 95 - 95: I1IiiI + i11iIiiIii
   self . paths [ 1 ] . addAnt ( self . tunnel . coords )
   if 6 - 6: ooOoO0o / i11iIiiIii + iII111i * oO0o
   if 80 - 80: II111iiii
  for Oo0o0000o0o0 in self . paths :
   Oo0o0000o0o0 . updateState ( currentState )
   if 83 - 83: I11i . i11iIiiIii + II111iiii . o0oOOo0O0Ooo * I11i
  oooO0 = iIIiIi1iIII1 . getQueen ( )
  if not oooO0 . hasMoved :
   return self . getQueenMove ( currentState )
   if 46 - 46: I1Ii111
   if 60 - 60: o0oOOo0O0Ooo
  if iIIiIi1iIII1 . foodCount > 0 :
   if getAntAt ( currentState , self . hill . coords ) is None :
    for Oo0o0000o0o0 in self . paths :
     if 25 - 25: OoO0O00
     if ( len ( Oo0o0000o0o0 . antList ) < 1 ) :
      Oo0o0000o0o0 . addAnt ( self . hill . coords )
      return Move ( BUILD , [ self . hill . coords ] , WORKER )
      if 62 - 62: OOooOOo + O0
      if 98 - 98: o0oOOo0O0Ooo
  for Oo0o0000o0o0 in self . paths :
   OOOO0oo0 = Oo0o0000o0o0 . updateNextAnt ( )
   if OOOO0oo0 is not None :
    return OOOO0oo0
    if 35 - 35: Ii1I - I1IiiI % o0oOOo0O0Ooo . OoooooooOO % Ii1I
  I1i1Iiiii = False
  if 94 - 94: o0oOOo0O0Ooo * Ii1I / Oo0Ooo / Ii1I
  if I1i1Iiiii == False :
   if 87 - 87: Oo0Ooo . IiII
   if ( II1I > 2 ) :
    self . CurDecision = 1
    I1i1Iiiii = True
    if 75 - 75: ooOoO0o + OoOoOO00 + o0oOOo0O0Ooo * I11i % oO0o . iII111i
    if 55 - 55: OOooOOo . I1IiiI
    if 61 - 61: Oo0Ooo % IiII . Oo0Ooo
    if 100 - 100: I1Ii111 * O0
    if 64 - 64: OOooOOo % iIii1I11I1II1 * oO0o
   elif ( len ( o00oooO0Oo ) >= 1 ) or ( len ( I11i1iIII ) >= 1 ) or ( len ( iiIiI ) >= 1 ) :
    iI1I111Ii111i = getConstrList ( currentState , OOoOO00OOO0OO , ( ANTHILL , ) ) [ 0 ]
    if 79 - 79: O0
    if 78 - 78: I1ii11iIi11i + OOooOOo - I1Ii111
    if len ( o00oooO0Oo ) >= 1 :
     for IIIIii1I in o00oooO0Oo :
      if IIIIii1I . coords [ 1 ] < ( iI1I111Ii111i . coords [ 1 ] ) :
       self . CurDecision = 2
       I1i1Iiiii = True
       if 39 - 39: II111iiii / ooOoO0o + I1Ii111 / OoOoOO00
    if len ( o00oooO0Oo ) >= 2 :
     for IIIIii1I in o00oooO0Oo :
      if IIIIii1I . coords [ 1 ] > ( iI1I111Ii111i . coords [ 1 ] ) :
       self . CurDecision = 3
       I1i1Iiiii = True
       if 13 - 13: IiII + O0 + iII111i % I1IiiI / o0oOOo0O0Ooo . IiII
       if 86 - 86: oO0o * o0oOOo0O0Ooo % i1IIi . Ii1I . i11iIiiIii
       if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
    if len ( I11i1iIII ) >= 1 :
     for O00o0OO0 in I11i1iIII :
      if O00o0OO0 . coords [ 1 ] < ( iI1I111Ii111i . coords [ 1 ] ) :
       self . CurDecision = 2
       I1i1Iiiii = True
       if 35 - 35: oO0o % ooOoO0o / I1Ii111 + iIii1I11I1II1 . OoooooooOO . I1IiiI
    if len ( I11i1iIII ) >= 2 :
     for O00o0OO0 in I11i1iIII :
      if O00o0OO0 . coords [ 1 ] > ( iI1I111Ii111i . coords [ 1 ] ) :
       self . CurDecision = 3
       I1i1Iiiii = True
       if 71 - 71: IiII * II111iiii * oO0o
       if 56 - 56: I1IiiI
    if len ( iiIiI ) >= 1 :
     for O0oO in iiIiI :
      if O0oO . coords [ 1 ] < ( iI1I111Ii111i . coords [ 1 ] ) :
       self . CurDecision = 2
       I1i1Iiiii = True
       if 73 - 73: I1ii11iIi11i * i11iIiiIii % oO0o . I1ii11iIi11i
    if len ( iiIiI ) >= 2 :
     for O0oO in iiIiI :
      if O0oO . coords [ 1 ] > ( iI1I111Ii111i . coords [ 1 ] ) :
       self . CurDecision = 3
       I1i1Iiiii = True
       if 66 - 66: oO0o + oO0o + ooOoO0o / iII111i + OOooOOo
       if 30 - 30: O0
       if 44 - 44: oO0o / I11i / I11i
       if 87 - 87: Oo0Ooo . I1IiiI - II111iiii + O0 / Oo0Ooo / oO0o
  if self . CurDecision == 1 :
   return self . starveMode ( currentState )
   if 25 - 25: I1IiiI . I1IiiI - OoOoOO00 % OoOoOO00 - i11iIiiIii / I1Ii111
  elif self . CurDecision == 2 :
   return self . defenseMode ( currentState )
   if 51 - 51: Oo0Ooo / OoOoOO00 . OOooOOo * o0oOOo0O0Ooo + OoO0O00 * IiII
  elif self . CurDecision == 3 :
   return self . gatherMode ( currentState )
   if 73 - 73: OoO0O00 + OoooooooOO - O0 - Ii1I - II111iiii
  return Move ( END , None , None )
  if 99 - 99: ooOoO0o . Ii1I + I1Ii111 + OoooooooOO % o0oOOo0O0Ooo
  if 51 - 51: iIii1I11I1II1
  if 34 - 34: oO0o + I1IiiI - oO0o
  if 17 - 17: II111iiii % iII111i + I11i - iII111i / OOooOOo + ooOoO0o
  if 59 - 59: OOooOOo % OoOoOO00 . Ii1I * I1ii11iIi11i % I11i
  if 59 - 59: oO0o - iII111i
  if 15 - 15: I1Ii111 . i11iIiiIii . OoooooooOO / OoO0O00 % Ii1I
  if 93 - 93: O0 % i1IIi . OOooOOo / I1IiiI - I1Ii111 / I1IiiI
  if 36 - 36: oO0o % oO0o % i1IIi / i1IIi - ooOoO0o
  if 30 - 30: I11i / I1IiiI
  if 35 - 35: II111iiii % OOooOOo . ooOoO0o + ooOoO0o % II111iiii % II111iiii
  if 72 - 72: II111iiii + i1IIi + o0oOOo0O0Ooo
  if 94 - 94: oO0o . i1IIi - o0oOOo0O0Ooo % O0 - OoO0O00
  if 72 - 72: Ii1I
  if 1 - 1: OoO0O00 * IiII * OoooooooOO + ooOoO0o
  if 33 - 33: O0 * o0oOOo0O0Ooo - I1Ii111 % I1Ii111
  if 18 - 18: I1Ii111 / Oo0Ooo * I1Ii111 + I1Ii111 * i11iIiiIii * I1ii11iIi11i
  if 11 - 11: ooOoO0o / OoOoOO00 - IiII * OoooooooOO + OoooooooOO . OoOoOO00
  if 26 - 26: Ii1I % I1ii11iIi11i
  if 76 - 76: IiII * iII111i
  if 52 - 52: OOooOOo
 def getAttack ( self , currentState , attackingAnt , enemyLocations ) :
  return enemyLocations [ 0 ]
  if 19 - 19: I1IiiI
  if 25 - 25: Ii1I / ooOoO0o
  if 31 - 31: OOooOOo . O0 % I1IiiI . o0oOOo0O0Ooo + IiII
  if 71 - 71: I1Ii111 . II111iiii
  if 62 - 62: OoooooooOO . I11i
  if 61 - 61: OoOoOO00 - OOooOOo - i1IIi
  if 25 - 25: O0 * I11i + I1ii11iIi11i . o0oOOo0O0Ooo . o0oOOo0O0Ooo
  if 58 - 58: I1IiiI
  if 53 - 53: i1IIi
  if 59 - 59: o0oOOo0O0Ooo
 def registerWin ( self , hasWon ) :
  if 81 - 81: OoOoOO00 - OoOoOO00 . iII111i
  pass
  if 73 - 73: I11i % i11iIiiIii - I1IiiI
  if 7 - 7: O0 * i11iIiiIii * Ii1I + ooOoO0o % OoO0O00 - ooOoO0o
  if 39 - 39: Oo0Ooo * OOooOOo % OOooOOo - OoooooooOO + o0oOOo0O0Ooo - I11i
  if 23 - 23: i11iIiiIii
  if 30 - 30: o0oOOo0O0Ooo - i1IIi % II111iiii + I11i * iIii1I11I1II1
  if 81 - 81: IiII % i1IIi . iIii1I11I1II1
  if 4 - 4: i11iIiiIii % OoO0O00 % i1IIi / IiII
  if 6 - 6: iII111i / I1IiiI % OOooOOo - I1IiiI
 def starveMode ( self , currentState ) :
  if 31 - 31: OOooOOo
  iIIiIi1iIII1 = getCurrPlayerInventory ( currentState )
  Ooo = currentState . whoseTurn
  if 23 - 23: I1Ii111 . IiII
  if 92 - 92: OoOoOO00 + I1Ii111 * Ii1I % I1IiiI
  if 42 - 42: Oo0Ooo
  if self . hill is None :
   self . hill = getConstrList ( currentState , Ooo , ( ANTHILL , ) ) [ 0 ]
  if self . tunnel is None :
   self . tunnel = getConstrList ( currentState , Ooo , ( TUNNEL , ) ) [ 0 ]
  if self . paths is None :
   if 76 - 76: I1IiiI * iII111i % I1Ii111
   self . paths = [ 0 for oo in range ( 2 ) ]
   if 57 - 57: iIii1I11I1II1 - i1IIi / I1Ii111 - O0 * OoooooooOO % II111iiii
   Oo00OO0o0o00 = getConstrList ( currentState , None , ( FOOD , ) )
   iI1Iii = [ ]
   for IiIi1I1 in Oo00OO0o0o00 :
    if isPathOkForQueen ( [ IiIi1I1 . coords ] ) :
     iI1Iii . append ( IiIi1I1 )
   self . foods = iI1Iii
   oO00OOoO00 = 999
   IiI111111IIII = None
   for i1Ii in iI1Iii :
    ii111iI1iIi1 = stepsToReach ( currentState , self . tunnel . coords , i1Ii . coords )
    if ii111iI1iIi1 < oO00OOoO00 :
     oO00OOoO00 = ii111iI1iIi1
     IiI111111IIII = i1Ii . coords
     if 39 - 39: II111iiii + OoOoOO00 - ooOoO0o . OoOoOO00
   oO00OOoO00 = 999
   oO0O00OoOO0 = None
   for i1Ii in iI1Iii :
    ii111iI1iIi1 = stepsToReach ( currentState , self . hill . coords , i1Ii . coords )
    if ii111iI1iIi1 < oO00OOoO00 :
     oO00OOoO00 = ii111iI1iIi1
     oO0O00OoOO0 = i1Ii . coords
     if 84 - 84: OoO0O00 + i1IIi - II111iiii . I1ii11iIi11i * OoooooooOO + I1IiiI
   if IiI111111IIII == oO0O00OoOO0 :
    oO00OOoO00 = 999
    for i1Ii in iI1Iii :
     ii111iI1iIi1 = stepsToReach ( currentState , self . hill . coords , i1Ii . coords )
     if ii111iI1iIi1 < oO00OOoO00 :
      if i1Ii . coords != IiI111111IIII :
       oO00OOoO00 = ii111iI1iIi1
       oO0O00OoOO0 = i1Ii . coords
       if 38 - 38: OOooOOo + II111iiii % ooOoO0o % OoOoOO00 - Ii1I / OoooooooOO
   self . paths [ 0 ] = Iiii111Ii11I1 ( oO0O00OoOO0 , self . hill . coords )
   self . paths [ 1 ] = Iiii111Ii11I1 ( IiI111111IIII , self . tunnel . coords )
   if 73 - 73: o0oOOo0O0Ooo * O0 - i11iIiiIii
   self . paths [ 1 ] . addAnt ( self . tunnel . coords )
   if 85 - 85: Ii1I % iII111i + I11i / o0oOOo0O0Ooo . oO0o + OOooOOo
   if 62 - 62: i11iIiiIii + i11iIiiIii - o0oOOo0O0Ooo
  for Oo0o0000o0o0 in self . paths :
   Oo0o0000o0o0 . updateState ( currentState )
   if 28 - 28: iII111i . iII111i % iIii1I11I1II1 * iIii1I11I1II1 . o0oOOo0O0Ooo / iII111i
   if 27 - 27: OoO0O00 + ooOoO0o - i1IIi
  oooO0 = iIIiIi1iIII1 . getQueen ( )
  if not oooO0 . hasMoved :
   O00oOOooo = getAntList ( currentState , 1 - Ooo , ( DRONE , SOLDIER , R_SOLDIER ) )
   iI1iIii11Ii = [ IIi1i1I11Iii . coords for IIi1i1I11Iii in O00oOOooo ]
   if 25 - 25: IiII + Ii1I / ooOoO0o . o0oOOo0O0Ooo % O0 * OoO0O00
   if len ( iI1iIii11Ii ) < 1 or len ( getAntList ( currentState , Ooo , ( WORKER , ) ) ) == 0 :
    o0O0oo0OO0O = [ ( 4 , 3 ) , ( 5 , 3 ) ] [ random . randint ( 0 , 1 ) ]
    Oo0o0000o0o0 = createPathToward ( currentState , oooO0 . coords ,
 o0O0oo0OO0O , UNIT_STATS [ QUEEN ] [ MOVEMENT ] )
    return Move ( MOVE_ANT , Oo0o0000o0o0 , None )
    if 68 - 68: oO0o . I11i % OoooooooOO . I11i
   OoooO = listAllMovementPaths ( currentState , oooO0 . coords , UNIT_STATS [ QUEEN ] [ MOVEMENT ] ,
 ignoresGrass = False )
   iIII = [ ]
   for iIi in OoooO :
    if isPathOkForQueen ( iIi ) and iIi [ - 1 ] not in [ ii111I . coords for ii111I in self . foods ] :
     iIII . append ( iIi )
     if 17 - 17: I1IiiI . O0 + OoO0O00
   ii = [ iIi [ - 1 ] for iIi in iIII ]
   if 25 - 25: OoooooooOO - I1IiiI . I1IiiI * oO0o
   o000oo = [ ]
   if 95 - 95: ooOoO0o / ooOoO0o
   for O00o0OO0 in range ( len ( ii ) ) :
    o000oo . append ( [ ] )
    for IIiI1Ii in iI1iIii11Ii :
     o000oo [ O00o0OO0 ] . append ( stepsToReach ( currentState , IIiI1Ii , ii [ O00o0OO0 ] ) )
   o000oo = [ min ( O00o0OO0 ) for O00o0OO0 in o000oo ]
   if 57 - 57: OOooOOo - ooOoO0o - I11i + OoO0O00
   Oo0o0000o0o0 = iIII [ o000oo . index ( max ( o000oo ) ) ] if 1 not in o000oo else iIII [ o000oo . index ( 1 ) ]
   return Move ( MOVE_ANT , Oo0o0000o0o0 , None )
   if 30 - 30: Ii1I % OoOoOO00 + i1IIi - I11i - Ii1I
  III11I1 = R_SOLDIER
  IIi1IIIi = UNIT_STATS [ III11I1 ] [ COST ]
  if 99 - 99: Ii1I + OoO0O00 * II111iiii . o0oOOo0O0Ooo - I1ii11iIi11i
  if iIIiIi1iIII1 . foodCount >= IIi1IIIi :
   if getAntAt ( currentState , self . hill . coords ) is None :
    if 58 - 58: Ii1I + o0oOOo0O0Ooo - I1IiiI
    OOoOO00OOO0OO = 1 - Ooo
    O00oOOooo = getAntList ( currentState , OOoOO00OOO0OO , ( WORKER , DRONE , SOLDIER , R_SOLDIER ) )
    i1i1ii = 0
    iII1ii1 = False
    for i11 in O00oOOooo :
     if i11 . coords [ 1 ] < 6 :
      i1i1ii += 1
     if stepsToReach ( currentState , i11 . coords , self . hill . coords ) <= UNIT_STATS [ i11 . type ] [ RANGE ] + UNIT_STATS [ i11 . type ] [ MOVEMENT ] + 1 :
      if 12 - 12: OOooOOo - ooOoO0o . OoooooooOO / I1ii11iIi11i . i1IIi * OoO0O00
      iII1ii1 = True
      break
    IiIiII1 = getAntList ( currentState , Ooo , ( III11I1 , ) )
    Iii1iiIi1II = [ IIi1i1I11Iii . coords for IIi1i1I11Iii in IiIiII1 ]
    if len ( IiIiII1 ) < 2 and not iII1ii1 :
     OO0O00oOo = False
     for oo in range ( len ( self . occupants ) ) :
      IIi1i1I11Iii = self . occupants [ oo ]
      if IIi1i1I11Iii is None or IIi1i1I11Iii not in Iii1iiIi1II :
       self . occupants [ oo ] = self . hill . coords
       OO0O00oOo = True
       break
     if not OO0O00oOo :
      for oo in range ( len ( self . occupants ) ) :
       IIi1i1I11Iii = self . occupants [ oo ]
       if self . occupants [ 0 ] == self . occupants [ 1 ] :
        self . occupants = [ self . hill . coords , self . occupants [ 1 ] ]
       elif len ( Iii1iiIi1II ) == 0 :
        self . occupants = [ self . hill . coords , None ]
       elif len ( Iii1iiIi1II ) == 1 :
        [ Iii1iiIi1II [ 0 ] , None ]
       elif len ( Iii1iiIi1II ) == 2 :
        self . occupants = Iii1iiIi1II
     return Move ( BUILD , [ self . hill . coords ] , III11I1 )
     if 14 - 14: I1IiiI
     if 19 - 19: OoO0O00 - Oo0Ooo . oO0o / oO0o % ooOoO0o
     if 56 - 56: I1IiiI . O0 + Oo0Ooo
  i1II1I1Iii1 = getAntList ( currentState , Ooo , ( III11I1 , ) )
  for iiI11Iii in i1II1I1Iii1 :
   if not iiI11Iii . hasMoved :
    OOoOO00OOO0OO = 1 - Ooo
    O00oOOooo = getAntList ( currentState , OOoOO00OOO0OO , ( WORKER , DRONE , SOLDIER , R_SOLDIER ) )
    if 78 - 78: iII111i + I11i . ooOoO0o - iII111i . Ii1I
    if 30 - 30: I1IiiI + OoO0O00 % Ii1I * iII111i / Oo0Ooo - I11i
    oO00OOoO00 = 999
    ooo = None
    iIi1i = None
    for i11 in O00oOOooo :
     I1i11111i1i11 = stepsToReach ( currentState , i11 . coords , iiI11Iii . coords )
     if I1i11111i1i11 < oO00OOoO00 :
      oO00OOoO00 = I1i11111i1i11
      ooo = i11
     if i11 . type != WORKER and stepsToReach ( currentState , ( i11 . coords [ 0 ] , self . hill . coords [ 1 ] ) , i11 . coords ) <= 2 :
      if 77 - 77: I1ii11iIi11i + OoO0O00 / oO0o + O0 * o0oOOo0O0Ooo
      iIi1i = i11 . coords
      if 28 - 28: ooOoO0o + i11iIiiIii / I11i % OoOoOO00 % Oo0Ooo - O0
    oo = self . occupants . index ( iiI11Iii . coords )
    oo = oo % 2
    if 54 - 54: i1IIi + II111iiii
    ooo = self . o_food [ oo ]
    oOOO0oo0 = getAntList ( currentState , OOoOO00OOO0OO , ( WORKER , ) )
    iIi1i1iIi1iI = getAntList ( currentState , OOoOO00OOO0OO , ( QUEEN , ) ) [ 0 ] . coords
    ii111I = stepsToReach ( currentState , iiI11Iii . coords , iIi1i1iIi1iI )
    if 26 - 26: OoooooooOO * I1IiiI + OOooOOo
    if ii111I < UNIT_STATS [ III11I1 ] [ RANGE ] :
     ooo = ( iiI11Iii . coords [ 0 ] , 4 )
     if 24 - 24: i11iIiiIii % iIii1I11I1II1 + OOooOOo / i11iIiiIii
    elif ii111I <= UNIT_STATS [ III11I1 ] [ RANGE ] + 1 :
     ooo = iiI11Iii . coords
     if 70 - 70: OoO0O00 * O0 . I11i + I1IiiI . IiII
    elif len ( oOOO0oo0 ) == 1 and not isPathOkForQueen ( [ iiI11Iii . coords ] ) :
     ooo = oOOO0oo0 [ 0 ] . coords
     if 14 - 14: iIii1I11I1II1 % iIii1I11I1II1 * i11iIiiIii - OoO0O00 - I11i
    elif len ( oOOO0oo0 ) == 0 or len ( getAntList ( currentState , Ooo , ( WORKER , ) ) ) == 0 and iIIiIi1iIII1 . foodCount < 1 :
     if 63 - 63: OoO0O00
     ooo = iIi1i1iIi1iI
     if 69 - 69: iIii1I11I1II1 . I1ii11iIi11i % ooOoO0o + iIii1I11I1II1 / O0 / I1ii11iIi11i
    elif iIi1i :
     ooo = iIi1i
     if 61 - 61: OOooOOo % OOooOOo * o0oOOo0O0Ooo / o0oOOo0O0Ooo
    elif len ( O00oOOooo ) - len ( oOOO0oo0 ) > 1 :
     ooo = ( iiI11Iii . coords [ 0 ] , 3 ) if iiI11Iii . coords [ 1 ] != 3 else ( random . randint ( 0 , 9 ) , 3 )
    if ooo is not None :
     Oo0o0000o0o0 = createPathToward ( currentState , iiI11Iii . coords , ooo , UNIT_STATS [ III11I1 ] [ MOVEMENT ] )
     if 75 - 75: IiII . ooOoO0o
     self . occupants [ oo ] = Oo0o0000o0o0 [ - 1 ]
     return Move ( MOVE_ANT , Oo0o0000o0o0 , None )
     if 50 - 50: OoOoOO00
     if 60 - 60: ooOoO0o * iIii1I11I1II1 * I1ii11iIi11i * Oo0Ooo
     if 69 - 69: Ii1I * O0 . i11iIiiIii / Ii1I . o0oOOo0O0Ooo
     if 63 - 63: I11i + o0oOOo0O0Ooo . II111iiii - I1IiiI
     if 52 - 52: o0oOOo0O0Ooo % Oo0Ooo
     if 64 - 64: O0 % I11i % O0 * OoO0O00 . oO0o + I1IiiI
     if 75 - 75: I11i . OoooooooOO % o0oOOo0O0Ooo * I11i % OoooooooOO
     if 13 - 13: IiII / i11iIiiIii % II111iiii % I11i . I1ii11iIi11i
     if 8 - 8: OoOoOO00 + Oo0Ooo - II111iiii
     if 11 - 11: i1IIi % i11iIiiIii - i1IIi * OoOoOO00
     if 39 - 39: I1Ii111
     if 86 - 86: I11i * I1IiiI + I11i + II111iiii
     if 8 - 8: I1Ii111 - iII111i / ooOoO0o
     if 96 - 96: OoOoOO00
     if 29 - 29: I1ii11iIi11i / i1IIi . I1IiiI - OoOoOO00 - OoOoOO00 - Ii1I
     if 20 - 20: i1IIi % OoO0O00 . I1IiiI / IiII * i11iIiiIii * OOooOOo
     if 85 - 85: o0oOOo0O0Ooo . OoOoOO00 / ooOoO0o . O0 % I1Ii111
     if 90 - 90: Oo0Ooo % O0 * iIii1I11I1II1 . iII111i
  for Oo0o0000o0o0 in self . paths :
   OOOO0oo0 = Oo0o0000o0o0 . updateNextAnt ( )
   if OOOO0oo0 is not None :
    return OOOO0oo0
    if 8 - 8: ooOoO0o + II111iiii / iII111i / I11i
  return Move ( END , None , None )
  if 74 - 74: O0 / i1IIi
  if 78 - 78: OoooooooOO . OoO0O00 + ooOoO0o - i1IIi
  if 31 - 31: OoooooooOO . OOooOOo
  if 83 - 83: iII111i . O0 / Oo0Ooo / OOooOOo - II111iiii
  if 100 - 100: OoO0O00
  if 46 - 46: OoOoOO00 / iIii1I11I1II1 % iII111i . iIii1I11I1II1 * iII111i
  if 38 - 38: I1ii11iIi11i - iII111i / O0 . I1Ii111
 def defenseMode ( self , currentState ) :
  if 45 - 45: I1Ii111
  iIIiIi1iIII1 = getCurrPlayerInventory ( currentState )
  Ooo = currentState . whoseTurn
  if 83 - 83: OoOoOO00 . OoooooooOO
  if 58 - 58: i11iIiiIii + OoooooooOO % OoooooooOO / IiII / i11iIiiIii
  if self . hill is None :
   self . hill = getConstrList ( currentState , Ooo , ( ANTHILL , ) ) [ 0 ]
  if self . tunnel is None :
   self . tunnel = getConstrList ( currentState , Ooo , ( TUNNEL , ) ) [ 0 ]
  if self . paths is None :
   if 62 - 62: OoO0O00 / I1ii11iIi11i
   self . paths = [ 0 for oo in range ( 2 ) ]
   if 7 - 7: OoooooooOO . IiII
   iI1Iii = getConstrList ( currentState , None , ( FOOD , ) )
   oO00OOoO00 = 999
   IiI111111IIII = None
   for i1Ii in iI1Iii :
    ii111iI1iIi1 = stepsToReach ( currentState , self . tunnel . coords , i1Ii . coords )
    if ii111iI1iIi1 < oO00OOoO00 :
     oO00OOoO00 = ii111iI1iIi1
     IiI111111IIII = i1Ii . coords
     if 53 - 53: Ii1I % Ii1I * o0oOOo0O0Ooo + OoOoOO00
   oO00OOoO00 = 999
   oO0O00OoOO0 = None
   for i1Ii in iI1Iii :
    ii111iI1iIi1 = stepsToReach ( currentState , self . hill . coords , i1Ii . coords )
    if ii111iI1iIi1 < oO00OOoO00 :
     oO00OOoO00 = ii111iI1iIi1
     oO0O00OoOO0 = i1Ii . coords
     if 92 - 92: OoooooooOO + i1IIi / Ii1I * O0
   if IiI111111IIII == oO0O00OoOO0 :
    oO00OOoO00 = 999
    for i1Ii in iI1Iii :
     ii111iI1iIi1 = stepsToReach ( currentState , self . hill . coords , i1Ii . coords )
     if ii111iI1iIi1 < oO00OOoO00 :
      if i1Ii . coords != IiI111111IIII :
       oO00OOoO00 = ii111iI1iIi1
       oO0O00OoOO0 = i1Ii . coords
       if 100 - 100: ooOoO0o % iIii1I11I1II1 * II111iiii - iII111i
   self . paths [ 0 ] = Iiii111Ii11I1 ( oO0O00OoOO0 , self . hill . coords )
   self . paths [ 1 ] = Iiii111Ii11I1 ( IiI111111IIII , self . tunnel . coords )
   if 92 - 92: ooOoO0o
   self . paths [ 1 ] . addAnt ( self . tunnel . coords )
   if 22 - 22: Oo0Ooo % iII111i * I1ii11iIi11i / OOooOOo % i11iIiiIii * I11i
   if 95 - 95: OoooooooOO - IiII * I1IiiI + OoOoOO00
  for Oo0o0000o0o0 in self . paths :
   Oo0o0000o0o0 . updateState ( currentState )
   if 10 - 10: o0oOOo0O0Ooo / i11iIiiIii
   if 92 - 92: I11i . I1Ii111
  oooO0 = iIIiIi1iIII1 . getQueen ( )
  if not oooO0 . hasMoved :
   return self . getQueenMove ( currentState )
   if 85 - 85: I1ii11iIi11i . I1Ii111
  O0O0Ooooo000 = R_SOLDIER
  if 65 - 65: OOooOOo * I1Ii111
  if 79 - 79: OoooooooOO - I1IiiI
  if 69 - 69: I11i
  if iIIiIi1iIII1 . foodCount > 1 :
   if getAntAt ( currentState , self . hill . coords ) is None :
    if 95 - 95: ooOoO0o + i11iIiiIii * I1Ii111 - i1IIi * I1Ii111 - iIii1I11I1II1
    OOoOO00OOO0OO = 1 - Ooo
    O00oOOooo = getAntList ( currentState , OOoOO00OOO0OO , ( DRONE , SOLDIER , R_SOLDIER ) )
    i1i1ii = len ( O00oOOooo )
    IiIiII1 = getAntList ( currentState , Ooo , ( O0O0Ooooo000 , ) )
    if len ( IiIiII1 ) <= i1i1ii :
     return Move ( BUILD , [ self . hill . coords ] , O0O0Ooooo000 )
     if 75 - 75: OoooooooOO * IiII
     if 9 - 9: IiII - II111iiii + O0 / iIii1I11I1II1 / i11iIiiIii
  I1IIIiI1I1ii1 = getAntAt ( currentState , self . hill . coords )
  if I1IIIiI1I1ii1 is not None and I1IIIiI1I1ii1 . player == currentState . whoseTurn :
   if I1IIIiI1I1ii1 . type == O0O0Ooooo000 :
    if not I1IIIiI1I1ii1 . hasMoved :
     Oo0o0000o0o0 = createPathToward ( currentState , I1IIIiI1I1ii1 . coords , ( 6 , 3 ) ,
 UNIT_STATS [ O0O0Ooooo000 ] [ MOVEMENT ] )
     return Move ( MOVE_ANT , Oo0o0000o0o0 , None )
     if 30 - 30: O0 * OoooooooOO
     if 38 - 38: IiII - I1ii11iIi11i . OoOoOO00 - I1Ii111 . OoooooooOO
  iI1Iii = getConstrList ( currentState , None , ( FOOD , ) )
  I1IIIiI1I1ii1 = [ getAntAt ( currentState , ii111I . coords ) for ii111I in iI1Iii ]
  for oooOooooO0oOO in I1IIIiI1I1ii1 :
   if oooOooooO0oOO is not None and oooOooooO0oOO . player == currentState . whoseTurn :
    if oooOooooO0oOO . type == O0O0Ooooo000 :
     if not oooOooooO0oOO . hasMoved :
      Oo0o0000o0o0 = createPathToward ( currentState , oooOooooO0oOO . coords , ( 7 , 3 ) , UNIT_STATS [ O0O0Ooooo000 ] [ MOVEMENT ] )
      return Move ( MOVE_ANT , Oo0o0000o0o0 , None )
      if 30 - 30: OoooooooOO - OoooooooOO . O0 / iII111i
      if 31 - 31: OOooOOo + o0oOOo0O0Ooo . OoooooooOO
  I1IIIiI1I1ii1 = getAntList ( currentState , Ooo , ( O0O0Ooooo000 , ) )
  for oooOooooO0oOO in I1IIIiI1I1ii1 :
   if not oooOooooO0oOO . hasMoved :
    OOoOO00OOO0OO = 1 - Ooo
    O00oOOooo = getAntList ( currentState , OOoOO00OOO0OO , ( QUEEN , DRONE , SOLDIER , R_SOLDIER ) )
    oO00OOoO00 = 999
    ooo = None
    for i11 in O00oOOooo :
     I1i11111i1i11 = stepsToReach ( currentState , i11 . coords , oooOooooO0oOO . coords )
     if I1i11111i1i11 < oO00OOoO00 :
      oO00OOoO00 = I1i11111i1i11
      ooo = i11
    if ooo is not None :
     ooOooo0 = aStarSearchPath ( currentState , oooOooooO0oOO . coords , ooo . coords )
     if ooOooo0 != False :
      Oo0o0000o0o0 = ooOooo0
     else :
      Oo0o0000o0o0 = createPathToward ( currentState , oooOooooO0oOO . coords , ooo . coords ,
 UNIT_STATS [ O0O0Ooooo000 ] [ MOVEMENT ] )
      if 67 - 67: I1IiiI
     return Move ( MOVE_ANT , Oo0o0000o0o0 , None )
     if 55 - 55: I1ii11iIi11i - iII111i * o0oOOo0O0Ooo + OoOoOO00 * OoOoOO00 * O0
     if 91 - 91: I1Ii111 - OOooOOo % iIii1I11I1II1 - OoooooooOO % ooOoO0o
  if iIIiIi1iIII1 . foodCount > 0 :
   if getAntAt ( currentState , self . hill . coords ) is None :
    for Oo0o0000o0o0 in self . paths :
     if len ( Oo0o0000o0o0 . antList ) == 0 :
      Oo0o0000o0o0 . addAnt ( self . hill . coords )
      if 98 - 98: OoO0O00 . OoO0O00 * oO0o * II111iiii * I1Ii111
      return Move ( BUILD , [ self . hill . coords ] , WORKER )
      if 92 - 92: Oo0Ooo
      if 40 - 40: OoOoOO00 / IiII
  for Oo0o0000o0o0 in self . paths :
   OOOO0oo0 = Oo0o0000o0o0 . updateNextAnt ( )
   if OOOO0oo0 is not None :
    return OOOO0oo0
    if 79 - 79: OoO0O00 - iIii1I11I1II1 + Ii1I - I1Ii111
  return Move ( END , None , None )
  if 93 - 93: II111iiii . I1IiiI - Oo0Ooo + OoOoOO00
  if 61 - 61: II111iiii
  if 15 - 15: i11iIiiIii % I1IiiI * I11i / I1Ii111
  if 90 - 90: iII111i
  if 31 - 31: OOooOOo + O0
  if 87 - 87: ooOoO0o
  if 45 - 45: OoO0O00 / OoooooooOO - iII111i / Ii1I % IiII
  if 83 - 83: I1IiiI . iIii1I11I1II1 - IiII * i11iIiiIii
 def gatherMode ( self , currentState ) :
  if 20 - 20: i1IIi * I1Ii111 + II111iiii % o0oOOo0O0Ooo % oO0o
  iIIiIi1iIII1 = getCurrPlayerInventory ( currentState )
  Ooo = currentState . whoseTurn
  if 13 - 13: Oo0Ooo
  if 60 - 60: I1ii11iIi11i * I1IiiI
  if self . hill is None :
   self . hill = getConstrList ( currentState , Ooo , ( ANTHILL , ) ) [ 0 ]
  if self . tunnel is None :
   self . tunnel = getConstrList ( currentState , Ooo , ( TUNNEL , ) ) [ 0 ]
  if self . paths is None :
   if 17 - 17: OOooOOo % Oo0Ooo / I1ii11iIi11i . IiII * OOooOOo - II111iiii
   self . paths = [ 0 for oo in range ( 2 ) ]
   if 41 - 41: Ii1I
   iI1Iii = getConstrList ( currentState , None , ( FOOD , ) )
   if 77 - 77: I1Ii111
   if 65 - 65: II111iiii . I1IiiI % oO0o * OoO0O00
   if 38 - 38: OoOoOO00 / iII111i % Oo0Ooo
   oO00OOoO00 = 999
   IiI111111IIII = None
   for i1Ii in iI1Iii :
    ii111iI1iIi1 = stepsToReach ( currentState , self . tunnel . coords , i1Ii . coords )
    if ii111iI1iIi1 < oO00OOoO00 :
     oO00OOoO00 = ii111iI1iIi1
     IiI111111IIII = i1Ii . coords
     if 11 - 11: iII111i - oO0o + II111iiii - iIii1I11I1II1
   oO00OOoO00 = 999
   oO0O00OoOO0 = None
   for i1Ii in iI1Iii :
    ii111iI1iIi1 = stepsToReach ( currentState , self . hill . coords , i1Ii . coords )
    if ii111iI1iIi1 < oO00OOoO00 and i1Ii . coords != IiI111111IIII :
     oO00OOoO00 = ii111iI1iIi1
     oO0O00OoOO0 = i1Ii . coords
     if 7 - 7: IiII - I11i / II111iiii * Ii1I . iII111i * iII111i
   self . paths [ 0 ] = Iiii111Ii11I1 ( oO0O00OoOO0 , self . hill . coords )
   self . paths [ 1 ] = Iiii111Ii11I1 ( IiI111111IIII , self . tunnel . coords )
   if 61 - 61: I11i % ooOoO0o - OoO0O00 / Oo0Ooo
   self . paths [ 1 ] . addAnt ( self . tunnel . coords )
   if 4 - 4: OoooooooOO - i1IIi % Ii1I - OOooOOo * o0oOOo0O0Ooo
   if 85 - 85: OoooooooOO * iIii1I11I1II1 . iII111i / OoooooooOO % I1IiiI % O0
  for Oo0o0000o0o0 in self . paths :
   Oo0o0000o0o0 . updateState ( currentState )
   if 36 - 36: Ii1I / II111iiii / IiII / IiII + I1ii11iIi11i
   if 95 - 95: IiII
  oooO0 = iIIiIi1iIII1 . getQueen ( )
  if not oooO0 . hasMoved :
   return self . getQueenMove ( currentState )
   if 51 - 51: II111iiii + IiII . i1IIi . I1ii11iIi11i + OoOoOO00 * I1IiiI
   if 72 - 72: oO0o + oO0o / II111iiii . OoooooooOO % Ii1I
   if 49 - 49: oO0o . OoO0O00 - Oo0Ooo * OoooooooOO . Oo0Ooo
   if 2 - 2: OoooooooOO % OOooOOo
   if 63 - 63: I1IiiI % iIii1I11I1II1
   if 39 - 39: iII111i / II111iiii / I1ii11iIi11i % I1IiiI
   if 89 - 89: I1Ii111 + OoooooooOO + I1Ii111 * i1IIi + iIii1I11I1II1 % I11i
   if 59 - 59: OOooOOo + i11iIiiIii
   if 88 - 88: i11iIiiIii - ooOoO0o
   if 67 - 67: OOooOOo . Oo0Ooo + OoOoOO00 - OoooooooOO
   if 70 - 70: OOooOOo / II111iiii - iIii1I11I1II1 - iII111i
   if 11 - 11: iIii1I11I1II1 . OoooooooOO . II111iiii / i1IIi - I11i
   if 30 - 30: OoOoOO00
   if 21 - 21: i11iIiiIii / I1Ii111 % OOooOOo * O0 . I11i - iIii1I11I1II1
   if 26 - 26: II111iiii * OoOoOO00
   if 10 - 10: II111iiii . iII111i
   if 32 - 32: Ii1I . IiII . OoooooooOO - OoO0O00 + oO0o
   if 88 - 88: iII111i
   if 19 - 19: II111iiii * IiII + Ii1I
   if 65 - 65: OOooOOo . I1Ii111 . OoO0O00 . iII111i - OOooOOo
   if 19 - 19: i11iIiiIii + iII111i % ooOoO0o
   if 14 - 14: OoO0O00 . II111iiii . I11i / Ii1I % I1ii11iIi11i - ooOoO0o
   if 67 - 67: I11i - OOooOOo . i1IIi
   if 35 - 35: iII111i + ooOoO0o - oO0o . iII111i . IiII
   if 87 - 87: OoOoOO00
   if 25 - 25: i1IIi . OoO0O00 - OoOoOO00 / OoO0O00 % OoO0O00 * iIii1I11I1II1
   if 50 - 50: OoO0O00 . i11iIiiIii - oO0o . oO0o
   if 31 - 31: OOooOOo / Oo0Ooo * i1IIi . OoOoOO00
   if 57 - 57: OOooOOo + iIii1I11I1II1 % i1IIi % I1IiiI
   if 83 - 83: o0oOOo0O0Ooo / i11iIiiIii % iIii1I11I1II1 . I11i % oO0o . OoooooooOO
   if 94 - 94: Ii1I + iIii1I11I1II1 % OoO0O00
   if 93 - 93: Ii1I - OOooOOo + iIii1I11I1II1 * o0oOOo0O0Ooo + I1Ii111 . iII111i
   if 49 - 49: OoooooooOO * I11i - Oo0Ooo . oO0o
   if 89 - 89: ooOoO0o + Ii1I * ooOoO0o / ooOoO0o
   if 46 - 46: OoO0O00
   if 71 - 71: I11i / I11i * oO0o * oO0o / II111iiii
  if 11 - len ( getAntList ( currentState , Ooo , [ WORKER ] ) ) > iIIiIi1iIII1 . foodCount > 0 :
   if getAntAt ( currentState , self . hill . coords ) is None :
    for Oo0o0000o0o0 in self . paths :
     if len ( Oo0o0000o0o0 . antList ) == 0 or len ( Oo0o0000o0o0 . antList ) < Oo0o0000o0o0 . dist / 2 :
      Oo0o0000o0o0 . addAnt ( self . hill . coords )
      return Move ( BUILD , [ self . hill . coords ] , WORKER )
      if 35 - 35: OOooOOo * o0oOOo0O0Ooo * I1IiiI % Oo0Ooo . OoOoOO00
      if 58 - 58: I11i + II111iiii * iII111i * i11iIiiIii - iIii1I11I1II1
  for Oo0o0000o0o0 in self . paths :
   OOOO0oo0 = Oo0o0000o0o0 . updateNextAnt ( )
   if OOOO0oo0 is not None :
    return OOOO0oo0
    if 68 - 68: OoooooooOO % II111iiii
  return Move ( END , None , None )
  if 26 - 26: II111iiii % i11iIiiIii % iIii1I11I1II1 % I11i * I11i * I1ii11iIi11i
  if 24 - 24: II111iiii % I1Ii111 - ooOoO0o + I1IiiI * I1ii11iIi11i
  if 2 - 2: Ii1I - IiII
  if 83 - 83: oO0o % o0oOOo0O0Ooo % Ii1I - II111iiii * OOooOOo / OoooooooOO
  if 18 - 18: OoO0O00 + iIii1I11I1II1 - II111iiii - I1IiiI
  if 71 - 71: OoooooooOO
  if 33 - 33: I1Ii111
 def getQueenMove ( self , state ) :
  iIIiIi1iIII1 = getCurrPlayerInventory ( state )
  Ooo = state . whoseTurn
  OOO0ooo = iIIiIi1iIII1 . getQueen ( )
  OOoOO00OOO0OO = 1 - Ooo
  IIiiii = getAntList ( state , OOoOO00OOO0OO , [ SOLDIER , R_SOLDIER , DRONE ] )
  if 37 - 37: o0oOOo0O0Ooo % ooOoO0o
  if 83 - 83: OOooOOo . I1Ii111 + oO0o - OOooOOo * I1Ii111 / I1Ii111
  if len ( IIiiii ) == 0 :
   return Move ( MOVE_ANT , createPathToward ( state , OOO0ooo . coords , ( 4 , 1 ) , UNIT_STATS [ QUEEN ] [ MOVEMENT ] ) , None )
   if 39 - 39: I1Ii111 / Oo0Ooo % OoO0O00 % i11iIiiIii
   if 90 - 90: I1Ii111 - OoooooooOO
   if 96 - 96: O0 . Ii1I % OoO0O00 * iIii1I11I1II1
  iI1Iii = getConstrList ( state , None , ( FOOD , ) )
  for i1Ii in iI1Iii :
   if OOO0ooo . coords == i1Ii . coords :
    Oo0o0000o0o0 = createPathToward ( state , OOO0ooo . coords , ( 7 , 3 ) , UNIT_STATS [ QUEEN ] [ MOVEMENT ] )
    return Move ( MOVE_ANT , Oo0o0000o0o0 , None )
    if 54 - 54: Ii1I * I1Ii111 - OoooooooOO % I1IiiI + O0
    if 6 - 6: I1ii11iIi11i - II111iiii / oO0o + i11iIiiIii + OOooOOo
  O0O0o0o0o = OOO0ooo . health
  IIIIIiI = OOO0ooo . coords
  oO00OOoO00 = 99
  Oo0000O0OOooO = None
  if 54 - 54: I11i / I1IiiI * oO0o + OoooooooOO - iII111i / OoooooooOO
  if 19 - 19: IiII * ooOoO0o * o0oOOo0O0Ooo + O0 / O0
  for i11 in IIiiii :
   ooOoO = ( i11 . coords [ 1 ] - 3 ) / UNIT_STATS [ i11 . type ] [ MOVEMENT ]
   if ooOoO < oO00OOoO00 :
    oO00OOoO00 = ooOoO
    Oo0000O0OOooO = i11
    if 91 - 91: oO0o + I1IiiI
  if Oo0000O0OOooO . coords [ 1 ] <= 4 :
   Oo0o0000o0o0 = createPathToward ( state , OOO0ooo . coords , ( Oo0000O0OOooO . coords [ 0 ] , min ( 3 , Oo0000O0OOooO . coords [ 1 ] ) ) , UNIT_STATS [ QUEEN ] [ MOVEMENT ] )
  elif Oo0000O0OOooO . type == R_SOLDIER :
   Oo0o0000o0o0 = createPathToward ( state , OOO0ooo . coords , ( Oo0000O0OOooO . coords [ 0 ] , 0 ) , UNIT_STATS [ QUEEN ] [ MOVEMENT ] )
  else :
   Oo0o0000o0o0 = createPathToward ( state , OOO0ooo . coords , ( Oo0000O0OOooO . coords [ 0 ] , 2 ) , UNIT_STATS [ QUEEN ] [ MOVEMENT ] )
   if 59 - 59: I1IiiI + i11iIiiIii + i1IIi / I11i
  return Move ( MOVE_ANT , Oo0o0000o0o0 , None )
  if 44 - 44: I11i . OoOoOO00 * I1IiiI + OoooooooOO - iII111i - IiII
  if 15 - 15: IiII / O0 . o0oOOo0O0Ooo . i11iIiiIii
  if 59 - 59: I1Ii111 - o0oOOo0O0Ooo - ooOoO0o
  if 48 - 48: i1IIi + I11i % OoOoOO00 / Oo0Ooo - o0oOOo0O0Ooo
  if 67 - 67: oO0o % o0oOOo0O0Ooo . OoooooooOO + OOooOOo * I11i * OoOoOO00
  if 36 - 36: O0 + Oo0Ooo
  if 5 - 5: Oo0Ooo * OoOoOO00
  if 46 - 46: ooOoO0o
  if 33 - 33: iII111i - II111iiii * OoooooooOO - Oo0Ooo - OOooOOo
  if 84 - 84: I1Ii111 + Oo0Ooo - OoOoOO00 * OoOoOO00
  if 61 - 61: OoooooooOO . oO0o . OoooooooOO / Oo0Ooo
  if 72 - 72: i1IIi
  if 82 - 82: OoOoOO00 + OoooooooOO / i11iIiiIii * I1ii11iIi11i . OoooooooOO
  if 63 - 63: I1ii11iIi11i
  if 6 - 6: ooOoO0o / I1ii11iIi11i
  if 57 - 57: I11i
  if 67 - 67: OoO0O00 . ooOoO0o
  if 87 - 87: oO0o % Ii1I
  if 83 - 83: II111iiii - I11i
  if 35 - 35: i1IIi - iIii1I11I1II1 + i1IIi
  if 86 - 86: iIii1I11I1II1 + OoOoOO00 . i11iIiiIii - Ii1I
  if 51 - 51: OoOoOO00
  if 14 - 14: IiII % oO0o % Oo0Ooo - i11iIiiIii
  if 53 - 53: Ii1I % Oo0Ooo
  if 59 - 59: OOooOOo % iIii1I11I1II1 . i1IIi + II111iiii * IiII
  if 41 - 41: Ii1I % I1ii11iIi11i
  if 12 - 12: OOooOOo
def ooOo0O ( coord ) :
 if 37 - 37: Ii1I % OoO0O00
 if 79 - 79: I1ii11iIi11i + I1IiiI / I1IiiI
 try :
  if len ( coord ) != 2 :
   return False
 except TypeError :
  print ( "ERROR:  parameter to legalCoord was not a tuple or list" )
  return False
  if 71 - 71: OOooOOo * OoO0O00 % OoooooooOO % OoO0O00 / I1IiiI
 ii111I = coord [ 0 ]
 Oo0ooo0Ooo = coord [ 1 ]
 return ( ( ii111I >= 0 ) and ( ii111I <= 9 ) and ( Oo0ooo0Ooo >= 0 ) and ( Oo0ooo0Ooo <= 9 ) )
 if 9 - 9: Oo0Ooo
 if 99 - 99: I11i - I1Ii111 - oO0o % OoO0O00
 if 21 - 21: II111iiii % I1ii11iIi11i . i1IIi - OoooooooOO
 if 4 - 4: OoooooooOO . ooOoO0o
 if 78 - 78: I1ii11iIi11i + I11i - O0
 if 10 - 10: I1Ii111 % I1IiiI
 if 97 - 97: OoooooooOO - I1Ii111
 if 58 - 58: iIii1I11I1II1 + O0
 if 30 - 30: ooOoO0o % iII111i * OOooOOo - I1ii11iIi11i * Ii1I % ooOoO0o
 if 46 - 46: i11iIiiIii - O0 . oO0o
 if 100 - 100: I1IiiI / o0oOOo0O0Ooo * iII111i . O0 / OOooOOo
 if 83 - 83: I1Ii111
 if 48 - 48: II111iiii * OOooOOo * I1Ii111
def i1iiiIii11 ( currentState ,
 pid = None ,
 types = ( QUEEN , WORKER , DRONE , SOLDIER , R_SOLDIER ) ) :
 if 67 - 67: o0oOOo0O0Ooo % OoOoOO00 . OoOoOO00 - ooOoO0o
 if 90 - 90: ooOoO0o + II111iiii * I1ii11iIi11i / Ii1I . o0oOOo0O0Ooo + o0oOOo0O0Ooo
 I11I = [ ]
 for oOoO in currentState . inventories :
  if ( pid == None ) or ( pid == oOoO . player ) :
   I11I += oOoO . ants
   if 26 - 26: OoOoOO00 / Oo0Ooo - i1IIi + I11i
   if 38 - 38: OoooooooOO / I1ii11iIi11i . O0 / i1IIi / Oo0Ooo + iIii1I11I1II1
 OOOO0oo0 = [ ]
 for i11 in I11I :
  if i11 . type in types :
   OOOO0oo0 . append ( i11 )
   if 96 - 96: iII111i
 return OOOO0oo0
 if 18 - 18: iII111i * I11i - Ii1I
 if 31 - 31: Oo0Ooo - O0 % OoOoOO00 % oO0o
 if 45 - 45: I1ii11iIi11i + II111iiii * i11iIiiIii
 if 13 - 13: OoooooooOO * oO0o - Ii1I / OOooOOo + I11i + IiII
 if 39 - 39: iIii1I11I1II1 - OoooooooOO
 if 81 - 81: I1ii11iIi11i - O0 * OoooooooOO
 if 23 - 23: II111iiii / oO0o
 if 28 - 28: Oo0Ooo * ooOoO0o - OoO0O00
 if 19 - 19: I11i
 if 67 - 67: O0 % iIii1I11I1II1 / IiII . i11iIiiIii - Ii1I + O0
 if 27 - 27: OOooOOo
 if 89 - 89: II111iiii / oO0o
 if 14 - 14: OOooOOo . I1IiiI * ooOoO0o + II111iiii - ooOoO0o + OOooOOo
 if 18 - 18: oO0o - o0oOOo0O0Ooo - I1IiiI - I1IiiI
 if 54 - 54: Oo0Ooo + I1IiiI / iII111i . I1IiiI * OoOoOO00
 if 1 - 1: OoOoOO00 * OoO0O00 . i1IIi / Oo0Ooo . I1ii11iIi11i + Oo0Ooo
def IIiIi1 ( currentState ,
 pid = None ,
 types = ( ANTHILL , TUNNEL , GRASS , FOOD ) ) :
 if 91 - 91: II111iiii % iII111i % IiII + II111iiii / oO0o
 if 62 - 62: OoooooooOO - i11iIiiIii
 Iii1 = [ ]
 for oOoO in currentState . inventories :
  if ( pid == None ) or ( pid == oOoO . player ) :
   Iii1 += oOoO . constrs
   if 73 - 73: OoOoOO00 . I1IiiI
   if 32 - 32: OoOoOO00 * I1IiiI % ooOoO0o * Ii1I . O0
 OOOO0oo0 = [ ]
 for i11i1i1I1iI1 in Iii1 :
  if i11i1i1I1iI1 . type in types :
   OOOO0oo0 . append ( i11i1i1I1iI1 )
   if 53 - 53: OOooOOo + I1IiiI / i11iIiiIii - o0oOOo0O0Ooo * oO0o / OoooooooOO
 return OOOO0oo0
 if 89 - 89: iIii1I11I1II1 / I1IiiI - II111iiii / Ii1I . i11iIiiIii . Ii1I
 if 48 - 48: O0 + O0 . I1Ii111 - ooOoO0o
 if 63 - 63: oO0o
 if 71 - 71: i1IIi . Ii1I * iII111i % OoooooooOO + OOooOOo
 if 36 - 36: IiII
 if 49 - 49: OOooOOo / OoooooooOO / I1IiiI
 if 74 - 74: I1Ii111 % I1ii11iIi11i
 if 7 - 7: II111iiii
 if 27 - 27: oO0o . OoooooooOO + i11iIiiIii
 if 86 - 86: I11i / o0oOOo0O0Ooo - o0oOOo0O0Ooo + I1ii11iIi11i + oO0o
 if 33 - 33: o0oOOo0O0Ooo . iII111i . IiII . i1IIi
 if 49 - 49: I1ii11iIi11i
def O0oOOo0o ( state , coords ) :
 if 50 - 50: iII111i . I1ii11iIi11i . OoO0O00 * I11i + II111iiii % i11iIiiIii
 Iii1 = getConstrList ( state )
 if 8 - 8: ooOoO0o * O0
 if 73 - 73: o0oOOo0O0Ooo / oO0o / I11i / OoO0O00
 for i11i1i1I1iI1 in Iii1 :
  if i11i1i1I1iI1 . coords == coords :
   return i11i1i1I1iI1
   if 11 - 11: OoOoOO00 + IiII - OoooooooOO / OoO0O00
 return None
 if 34 - 34: ooOoO0o
 if 45 - 45: ooOoO0o / Oo0Ooo / Ii1I
 if 44 - 44: I1ii11iIi11i - Ii1I / II111iiii * OoO0O00 * Oo0Ooo
 if 73 - 73: o0oOOo0O0Ooo - I1IiiI * i1IIi / i11iIiiIii * OOooOOo % II111iiii
 if 56 - 56: OoooooooOO * Oo0Ooo . Oo0Ooo . I1ii11iIi11i
 if 24 - 24: Oo0Ooo . I11i * Ii1I % iII111i / OOooOOo
 if 58 - 58: I1IiiI - I1ii11iIi11i % O0 . I1IiiI % OoO0O00 % IiII
 if 87 - 87: oO0o - i11iIiiIii
 if 78 - 78: i11iIiiIii / iIii1I11I1II1 - o0oOOo0O0Ooo
 if 23 - 23: I11i
 if 40 - 40: o0oOOo0O0Ooo - II111iiii / Oo0Ooo
 if 14 - 14: I1ii11iIi11i
def iI1 ( state , coords ) :
 if 14 - 14: I1ii11iIi11i
 I11I = getAntList ( state )
 if 49 - 49: oO0o / i1IIi % Ii1I . I1IiiI
 if 93 - 93: OOooOOo
 for i11 in I11I :
  if i11 . coords == coords :
   return i11
   if 43 - 43: I1ii11iIi11i / I1IiiI . ooOoO0o
 return None
 if 62 - 62: iIii1I11I1II1 + iII111i . Oo0Ooo / IiII % O0 . I1Ii111
 if 93 - 93: i11iIiiIii % iIii1I11I1II1 % i11iIiiIii + o0oOOo0O0Ooo / o0oOOo0O0Ooo / II111iiii
 if 49 - 49: OOooOOo . I1ii11iIi11i . i11iIiiIii - II111iiii / Ii1I
 if 62 - 62: OOooOOo
 if 1 - 1: IiII / IiII - i11iIiiIii
 if 87 - 87: Oo0Ooo / O0 * IiII / o0oOOo0O0Ooo
 if 19 - 19: I1Ii111 + i1IIi . I1IiiI - Oo0Ooo
 if 16 - 16: oO0o + ooOoO0o / o0oOOo0O0Ooo
 if 82 - 82: IiII * i11iIiiIii % II111iiii - OoooooooOO
 if 90 - 90: Oo0Ooo . oO0o * i1IIi - i1IIi
 if 16 - 16: I1IiiI * i1IIi - o0oOOo0O0Ooo . IiII % I11i / o0oOOo0O0Ooo
 if 14 - 14: iIii1I11I1II1 * I1Ii111 * I1ii11iIi11i / iIii1I11I1II1 * IiII / I11i
 if 77 - 77: OoO0O00 + I1Ii111 + I1Ii111 * Ii1I / OoooooooOO . Ii1I
def ooo0O0OO ( currentState ) :
 O0Oooo = currentState . whoseTurn
 oO000 = 1 - O0Oooo
 if 7 - 7: IiII * I1IiiI + i1IIi + i11iIiiIii + Oo0Ooo % I1IiiI
 iIIiIi1iIII1 = currentState . inventories [ O0Oooo ]
 OO00OO0o0 = currentState . inventories [ oO000 ]
 if 52 - 52: I1ii11iIi11i % oO0o - i11iIiiIii
 oooO0 = iIIiIi1iIII1 . getQueen ( )
 i1III = iIIiIi1iIII1 . getAnthill ( )
 I1I = iIIiIi1iIII1 . foodCount
 if 73 - 73: Ii1I
 OOO = OO00OO0o0 . getQueen ( )
 IiIi1111ii = OO00OO0o0 . getAnthill ( )
 iI1I1II1 = OO00OO0o0 . foodCount
 if 92 - 92: OoooooooOO - OoooooooOO * OoO0O00 % I1IiiI
 if IiIi1111ii . captureHealth <= 0 or I1I >= FOOD_GOAL or OOO is None or ( iI1I1II1 == 0 and len ( OO00OO0o0 . ants ) == 1 ) :
  return 1
  if 77 - 77: iIii1I11I1II1 - i1IIi . oO0o
 if i1III . captureHealth <= 0 or iI1I1II1 >= FOOD_GOAL or oooO0 is None or ( I1I == 0 and len ( iIIiIi1iIII1 . ants ) == 1 ) :
  return 0
  if 26 - 26: o0oOOo0O0Ooo * IiII . i1IIi
 return None
 if 59 - 59: O0 + i1IIi - o0oOOo0O0Ooo
 if 62 - 62: i11iIiiIii % OOooOOo . IiII . OOooOOo
 if 84 - 84: i11iIiiIii * OoO0O00
 if 18 - 18: OOooOOo - Ii1I - OoOoOO00 / I1Ii111 - O0
 if 30 - 30: O0 + I1ii11iIi11i + II111iiii
 if 14 - 14: o0oOOo0O0Ooo / OOooOOo - iIii1I11I1II1 - oO0o % ooOoO0o
 if 49 - 49: ooOoO0o * oO0o / o0oOOo0O0Ooo / Oo0Ooo * iIii1I11I1II1
 if 57 - 57: OoOoOO00 - oO0o / ooOoO0o % i11iIiiIii
 if 3 - 3: iII111i . ooOoO0o % I1IiiI + I1ii11iIi11i
 if 64 - 64: i1IIi
def IIii1 ( coord ) :
 if 35 - 35: i11iIiiIii - I1IiiI / OOooOOo + Ii1I * oO0o
 if not legalCoord ( coord ) :
  return [ ]
  if 49 - 49: o0oOOo0O0Ooo * Ii1I + I11i + iII111i
  if 30 - 30: o0oOOo0O0Ooo / OOooOOo / IiII % ooOoO0o + II111iiii
 I1III111i = [ ( - 1 , 0 ) , ( 1 , 0 ) , ( 0 , - 1 ) , ( 0 , 1 ) ]
 ii111I = coord [ 0 ]
 Oo0ooo0Ooo = coord [ 1 ]
 OOOO0oo0 = [ ]
 if 4 - 4: i1IIi + ooOoO0o + i1IIi
 if 31 - 31: Ii1I
 for OoOOo00 in I1III111i :
  O00 = OoOOo00 [ 0 ] + coord [ 0 ]
  O0O = OoOOo00 [ 1 ] + coord [ 1 ]
  if 72 - 72: I1Ii111 . I1ii11iIi11i % OoOoOO00 . i11iIiiIii
  if 53 - 53: I1ii11iIi11i / IiII / OoooooooOO / II111iiii
  if legalCoord ( ( O00 , O0O ) ) :
   OOOO0oo0 . append ( ( O00 , O0O ) )
   if 32 - 32: iIii1I11I1II1 . i11iIiiIii / oO0o
 return OOOO0oo0
 if 52 - 52: I1IiiI + iIii1I11I1II1
 if 71 - 71: O0 / oO0o
 if 34 - 34: OoOoOO00 . iIii1I11I1II1 % O0
 if 43 - 43: I1ii11iIi11i - iII111i
 if 70 - 70: iII111i / OOooOOo % ooOoO0o - Ii1I
 if 47 - 47: iII111i
 if 92 - 92: OOooOOo + OoOoOO00 % i1IIi
 if 23 - 23: I1Ii111 - OOooOOo + Ii1I - OoOoOO00 * OoOoOO00 . Oo0Ooo
 if 47 - 47: oO0o % iIii1I11I1II1
def IiI1IIIII1I ( coord , dist = 1 ) :
 I1I1IiIi1 = [ ]
 if 58 - 58: OoOoOO00 - iII111i - OoooooooOO
 if 96 - 96: iIii1I11I1II1
 for oo in range ( - dist , dist + 1 ) :
  if 82 - 82: OoOoOO00 + O0 - IiII % oO0o * i11iIiiIii
  if 15 - 15: o0oOOo0O0Ooo
  I1iI = dist - abs ( oo )
  for o00oOO0o in range ( - I1iI , I1iI + 1 ) :
   oO0Ooo0OooOOo = ( coord [ 0 ] + oo , coord [ 1 ] + o00oOO0o )
   if legalCoord ( oO0Ooo0OooOOo ) and oO0Ooo0OooOOo != coord :
    I1I1IiIi1 . append ( oO0Ooo0OooOOo )
    if 71 - 71: IiII + i1IIi * Oo0Ooo % Oo0Ooo / Oo0Ooo
 return I1I1IiIi1
 if 55 - 55: OoooooooOO + I1Ii111 + OoooooooOO * ooOoO0o
 if 68 - 68: O0
 if 2 - 2: OoO0O00 + O0 * OoO0O00 - Ii1I + oO0o
 if 43 - 43: I1ii11iIi11i - OoOoOO00
 if 36 - 36: I1ii11iIi11i - iII111i
 if 24 - 24: o0oOOo0O0Ooo + ooOoO0o + I11i - iIii1I11I1II1
 if 49 - 49: I11i . ooOoO0o * OoOoOO00 % IiII . O0
 if 48 - 48: O0 * Ii1I - O0 / Ii1I + OoOoOO00
 if 52 - 52: OoO0O00 % Ii1I * II111iiii
 if 4 - 4: I11i % O0 - OoooooooOO + ooOoO0o . oO0o % II111iiii
 if 9 - 9: II111iiii * II111iiii . i11iIiiIii * iIii1I11I1II1
 if 18 - 18: OoO0O00 . II111iiii % OoOoOO00 % Ii1I
 if 87 - 87: iIii1I11I1II1 . OoooooooOO * OoOoOO00
 if 100 - 100: OoO0O00 / i1IIi - I1IiiI % Ii1I - iIii1I11I1II1
 if 17 - 17: I11i / o0oOOo0O0Ooo % Oo0Ooo
def o0o ( state , coords , movement , ignoresGrass = False ) :
 if 93 - 93: ooOoO0o % i11iIiiIii % I1Ii111
 O00OooO = listAdjacent ( coords )
 if 40 - 40: I11i % OoooooooOO - OOooOOo + o0oOOo0O0Ooo / OOooOOo
 if 84 - 84: O0
 iiii = [ ]
 for I11I1i1iI in O00OooO :
  i11 = getAntAt ( state , I11I1i1iI )
  i11i1i1I1iI1 = getConstrAt ( state , I11I1i1iI )
  O00oO0O0oO00o = 1
  if i11i1i1I1iI1 != None and not ignoresGrass :
   O00oO0O0oO00o = CONSTR_STATS [ i11i1i1I1iI1 . type ] [ MOVE_COST ]
  if ( i11 == None ) and ( O00oO0O0oO00o <= movement ) :
   iiii . append ( I11I1i1iI )
   if 17 - 17: Ii1I
 return iiii
 if 39 - 39: ooOoO0o . II111iiii
 if 45 - 45: oO0o * OoOoOO00 / iIii1I11I1II1
 if 77 - 77: I1Ii111 - I11i
 if 11 - 11: I1ii11iIi11i
 if 26 - 26: iIii1I11I1II1 * I1Ii111 - OOooOOo
 if 27 - 27: I1ii11iIi11i * I1Ii111 - OoO0O00 + Ii1I * Ii1I
 if 55 - 55: ooOoO0o
 if 82 - 82: I1Ii111 - OOooOOo + OoO0O00
 if 64 - 64: o0oOOo0O0Ooo . O0 * Ii1I + OoooooooOO - Oo0Ooo . OoooooooOO
 if 70 - 70: Oo0Ooo - oO0o . iIii1I11I1II1 % I11i / OoOoOO00 - O0
 if 55 - 55: iII111i - OoO0O00
 if 100 - 100: O0
 if 79 - 79: iIii1I11I1II1
 if 81 - 81: OOooOOo + iIii1I11I1II1 * I1Ii111 - iIii1I11I1II1 . OOooOOo
 if 48 - 48: I11i . OoooooooOO . I1IiiI . OoOoOO00 % I1ii11iIi11i / iII111i
 if 11 - 11: i1IIi % OoO0O00 % iII111i
 if 99 - 99: ooOoO0o / iIii1I11I1II1 - Ii1I * I1ii11iIi11i % I1IiiI
def i1II1i ( currentState , coords , movement , ignoresGrass = False ) :
 if 10 - 10: Ii1I - OoOoOO00 . OoooooooOO . OOooOOo . OoO0O00 * iII111i
 if ( movement <= 0 ) : return [ ]
 if 78 - 78: oO0o / OoO0O00 - oO0o * OoooooooOO . OoOoOO00
 if 96 - 96: I1IiiI % i1IIi . o0oOOo0O0Ooo . O0
 Ii1Iii11 = listReachableAdjacent ( currentState , coords , movement , ignoresGrass )
 o0oO = [ ]
 for I11I1i1iI in Ii1Iii11 :
  o0oO . append ( [ coords , I11I1i1iI ] )
  if 29 - 29: iII111i + i11iIiiIii % I11i
  if 93 - 93: OoOoOO00 % iIii1I11I1II1
 Ooo0o0oo0 = list ( o0oO )
 if 87 - 87: OoOoOO00 / IiII + iIii1I11I1II1
 if 93 - 93: iIii1I11I1II1 + oO0o % ooOoO0o
 for i11iIIIIIi1 in o0oO :
  if 21 - 21: OOooOOo
  iIiI1I1IIi11 = i11iIIIIIi1 [ - 1 ]
  I1I1i11 = getConstrAt ( currentState , iIiI1I1IIi11 )
  i1IiIi1i = 1
  if I1I1i11 != None and not ignoresGrass :
   i1IiIi1i = CONSTR_STATS [ I1I1i11 . type ] [ MOVE_COST ]
   if 48 - 48: o0oOOo0O0Ooo . Ii1I + OoOoOO00 % I1ii11iIi11i / i11iIiiIii
   if 74 - 74: II111iiii . O0 - I1IiiI + IiII % i11iIiiIii % OoOoOO00
  O0OOO0 = listAllMovementPaths ( currentState , iIiI1I1IIi11 , movement - i1IiIi1i , ignoresGrass )
  if 8 - 8: i11iIiiIii / II111iiii + o0oOOo0O0Ooo * Ii1I % IiII . I11i
  if 6 - 6: IiII % Oo0Ooo . Oo0Ooo - I1ii11iIi11i / I11i . i1IIi
  for oO0 in O0OOO0 :
   O0oOIiIII = list ( i11iIIIIIi1 )
   for I11I1i1iI in oO0 [ 1 : ] :
    O0oOIiIII . append ( I11I1i1iI )
   Ooo0o0oo0 . append ( O0oOIiIII )
   if 13 - 13: o0oOOo0O0Ooo % oO0o / I1Ii111 % I1Ii111 % O0
   if 90 - 90: IiII . ooOoO0o / iIii1I11I1II1
 Ooo0o0oo0 . append ( [ coords ] )
 if 28 - 28: IiII + oO0o - ooOoO0o / iIii1I11I1II1 - I1IiiI
 return Ooo0o0oo0
 if 45 - 45: O0 / i1IIi * oO0o * OoO0O00
 if 35 - 35: I1ii11iIi11i / iII111i % I1IiiI + iIii1I11I1II1
 if 79 - 79: OoOoOO00 / ooOoO0o
 if 77 - 77: Oo0Ooo
 if 46 - 46: I1Ii111
 if 72 - 72: iII111i * OOooOOo
 if 67 - 67: i1IIi
 if 5 - 5: II111iiii . OoooooooOO
 if 57 - 57: I1IiiI
 if 35 - 35: OoooooooOO - I1Ii111 / OoO0O00
 if 50 - 50: OoOoOO00
 if 33 - 33: I11i
 if 98 - 98: OoOoOO00 % II111iiii
 if 95 - 95: iIii1I11I1II1 - I1Ii111 - OOooOOo + I1Ii111 % I1ii11iIi11i . I1IiiI
def IiiIIi1 ( currentState , src , dst ) :
 if 28 - 28: o0oOOo0O0Ooo
 if ( not legalCoord ( src ) ) : return - 1
 if ( not legalCoord ( dst ) ) : return - 1
 if 45 - 45: o0oOOo0O0Ooo . I1IiiI / I1Ii111 - Oo0Ooo * iIii1I11I1II1
 if 86 - 86: II111iiii + ooOoO0o + IiII
 I11i11I = { src : 0 }
 if 90 - 90: I1ii11iIi11i
 i11i11i = [ src ]
 if 41 - 41: I1ii11iIi11i + Ii1I % OoooooooOO . I1ii11iIi11i + iII111i . iII111i
 if 31 - 31: i11iIiiIii + II111iiii . iII111i * OoOoOO00
 while ( len ( i11i11i ) > 0 ) :
  I11I1i1iI = i11i11i . pop ( 0 )
  if 66 - 66: OoOoOO00 + i1IIi % II111iiii . O0 * I1ii11iIi11i % I1ii11iIi11i
  if 87 - 87: OOooOOo + o0oOOo0O0Ooo . iII111i - OoooooooOO
  if ( I11I1i1iI == dst ) :
   return I11i11I [ I11I1i1iI ]
   if 6 - 6: iIii1I11I1II1 * OoooooooOO
   if 28 - 28: Oo0Ooo * o0oOOo0O0Ooo / I1Ii111
   if 52 - 52: O0 / o0oOOo0O0Ooo % iII111i * I1IiiI % OOooOOo
  o0oOOOO0 = listAdjacent ( I11I1i1iI )
  for ii1I in o0oOOOO0 :
   I1I1i11 = getConstrAt ( currentState , ii1I )
   i1IiIi1i = 1
   if I1I1i11 != None :
    i1IiIi1i = CONSTR_STATS [ I1I1i11 . type ] [ MOVE_COST ]
   oO00OOoO00 = I11i11I [ I11I1i1iI ] + i1IiIi1i
   if 84 - 84: I1ii11iIi11i - iIii1I11I1II1 % O0 + iII111i
   if 93 - 93: Oo0Ooo / IiII % I1ii11iIi11i
   if ( ii1I in I11i11I ) :
    if ( oO00OOoO00 < I11i11I [ ii1I ] ) :
     I11i11I [ ii1I ] = oO00OOoO00
     if 77 - 77: i11iIiiIii % i1IIi % IiII
     if 15 - 15: iIii1I11I1II1 . O0
   else :
    I11i11I [ ii1I ] = oO00OOoO00
    i11i11i . append ( ii1I )
    if 70 - 70: Ii1I . i11iIiiIii % Ii1I . O0 - iIii1I11I1II1
    if 26 - 26: OOooOOo
 return - 1
 if 76 - 76: i1IIi * OoooooooOO * O0 + I1Ii111 * I1Ii111
 if 35 - 35: o0oOOo0O0Ooo
 if 73 - 73: O0 - I1ii11iIi11i
 if 2 - 2: II111iiii / I1Ii111
 if 54 - 54: i1IIi . I11i - I1ii11iIi11i + ooOoO0o + Oo0Ooo / Oo0Ooo
 if 22 - 22: ooOoO0o . iIii1I11I1II1
 if 12 - 12: Ii1I
 if 71 - 71: I1IiiI . II111iiii . I1IiiI - ooOoO0o
 if 45 - 45: IiII / O0 / OoOoOO00 * OOooOOo
 if 18 - 18: iIii1I11I1II1 + OOooOOo + iIii1I11I1II1 . I1ii11iIi11i + I1Ii111 . ooOoO0o
 if 7 - 7: I1ii11iIi11i + iIii1I11I1II1 * I11i * I11i / II111iiii - Ii1I
 if 65 - 65: oO0o + OoOoOO00 + II111iiii
 if 77 - 77: II111iiii
def Iii ( sourceCoords , targetCoords ) :
 return abs ( sourceCoords [ 0 ] - targetCoords [ 0 ] ) + abs ( sourceCoords [ 1 ] - targetCoords [ 1 ] )
 if 7 - 7: Oo0Ooo * OoooooooOO % O0 - Ii1I . Ii1I
 if 80 - 80: OoOoOO00 - II111iiii
 if 35 - 35: ooOoO0o - OoO0O00 . Oo0Ooo * Oo0Ooo / i11iIiiIii + I1ii11iIi11i
 if 87 - 87: OoOoOO00 % iIii1I11I1II1
 if 72 - 72: OOooOOo . OOooOOo - I1ii11iIi11i
 if 48 - 48: Oo0Ooo - ooOoO0o + Oo0Ooo - I1IiiI * i11iIiiIii . iII111i
 if 35 - 35: IiII . O0 + Oo0Ooo + OOooOOo + i1IIi
 if 65 - 65: O0 * I1IiiI / I1IiiI . OoOoOO00
 if 87 - 87: II111iiii * I1ii11iIi11i % Oo0Ooo * Oo0Ooo
 if 58 - 58: OOooOOo . o0oOOo0O0Ooo + I1IiiI % Oo0Ooo - OoO0O00
 if 50 - 50: iII111i % II111iiii - ooOoO0o . i1IIi + O0 % iII111i
 if 10 - 10: iII111i . i1IIi + Ii1I
 if 66 - 66: OoO0O00 % o0oOOo0O0Ooo
 if 21 - 21: OoOoOO00 - OoooooooOO % i11iIiiIii
 if 71 - 71: i1IIi - I11i * I1Ii111 + oO0o - OoO0O00 % I1ii11iIi11i
 if 63 - 63: iIii1I11I1II1 + OOooOOo . OoO0O00 / I1IiiI
def oO0O ( currentState , sourceCoords , targetCoords , movement ) :
 i11 = getAntAt ( currentState , sourceCoords )
 if 26 - 26: iIii1I11I1II1 + i1IIi / OoOoOO00 % I1ii11iIi11i
 if i11 is None :
  Ii = False
 else :
  Ii = UNIT_STATS [ i11 . type ] [ IGNORES_GRASS ]
 return findPathRecursive ( currentState , sourceCoords , targetCoords , movement , Ii ) [ 0 ]
 if 14 - 14: OOooOOo % OoooooooOO
 if 86 - 86: i11iIiiIii + O0 * IiII - OoO0O00 * OOooOOo + O0
 if 95 - 95: iIii1I11I1II1 . I1Ii111 % iII111i - I1Ii111 * II111iiii
 if 89 - 89: iII111i . I1IiiI
 if 59 - 59: i1IIi % iIii1I11I1II1 + OoooooooOO
 if 97 - 97: I1ii11iIi11i / Oo0Ooo + I1Ii111
 if 32 - 32: ooOoO0o % I1Ii111 * Oo0Ooo
 if 72 - 72: ooOoO0o . iII111i - I1Ii111 - Ii1I % i1IIi
 if 56 - 56: Oo0Ooo * iII111i
 if 13 - 13: Oo0Ooo * Oo0Ooo * II111iiii * iII111i . i1IIi / IiII
 if 92 - 92: Ii1I * i11iIiiIii + iII111i * I1Ii111
 if 48 - 48: I11i * iII111i * iII111i
 if 70 - 70: oO0o + I11i % i11iIiiIii + O0
 if 65 - 65: iIii1I11I1II1 % oO0o + O0 / OoooooooOO
 if 52 - 52: Ii1I % OOooOOo * I1IiiI % I11i + OOooOOo / iII111i
def oo000o ( state , source , target , movement , ignoresGrass ) :
 oO00OOoO00 = approxDist ( source , target )
 if oO00OOoO00 == 0 :
  return ( [ source ] , 0 )
 if movement == 0 :
  return ( [ source ] , oO00OOoO00 )
  if 95 - 95: oO0o - ooOoO0o * I11i / OoO0O00 / II111iiii + O0
 I1Ioo0o00oOo0 = ( [ source ] , oO00OOoO00 )
 for O0OOo in listReachableAdjacent ( state , source , movement , ignoresGrass ) :
  if 30 - 30: I1Ii111 - Oo0Ooo
  i1IiIi1i = 1
  if not ignoresGrass :
   ooI111iiiii1 = getConstrAt ( state , O0OOo )
   if ooI111iiiii1 is not None :
    i1IiIi1i = ooI111iiiii1 . movementCost
    if 100 - 100: I1ii11iIi11i * i11iIiiIii % oO0o / Oo0Ooo / ooOoO0o + I1ii11iIi11i
    if 59 - 59: I1Ii111 - IiII
  Oo0o0000o0o0 = findPathRecursive ( state , O0OOo , target , movement - i1IiIi1i , ignoresGrass )
  if 14 - 14: iIii1I11I1II1 - iIii1I11I1II1
  if 5 - 5: IiII
  if Oo0o0000o0o0 [ 1 ] < I1Ioo0o00oOo0 [ 1 ] :
   I1Ioo0o00oOo0 = ( [ source ] + Oo0o0000o0o0 [ 0 ] , Oo0o0000o0o0 [ 1 ] )
   if 84 - 84: II111iiii * oO0o * II111iiii % IiII / I1IiiI
   if I1Ioo0o00oOo0 [ 1 ] == 0 or I1Ioo0o00oOo0 [ 1 ] == oO00OOoO00 - movement :
    return I1Ioo0o00oOo0
 return I1Ioo0o00oOo0
 if 100 - 100: IiII . Ii1I - iIii1I11I1II1 . i11iIiiIii / II111iiii
 if 71 - 71: I1Ii111 * Oo0Ooo . I11i
 if 49 - 49: IiII * O0 . IiII
 if 19 - 19: II111iiii - IiII
 if 59 - 59: o0oOOo0O0Ooo * OoO0O00 - Ii1I . OOooOOo
 if 89 - 89: OOooOOo
 if 69 - 69: ooOoO0o - OoooooooOO * O0
 if 84 - 84: ooOoO0o + i11iIiiIii - OOooOOo * ooOoO0o
 if 33 - 33: ooOoO0o % i1IIi - oO0o . O0 / O0
 if 96 - 96: OoooooooOO + IiII * O0
 if 86 - 86: Ii1I
 if 29 - 29: iIii1I11I1II1 - OoO0O00 + I1IiiI % iIii1I11I1II1 % OOooOOo
def O0OOO00 ( currentState ) :
 OOOO0oo0 = [ ]
 if 62 - 62: i11iIiiIii + OoOoOO00 + i1IIi
 if 69 - 69: OoOoOO00
 if 63 - 63: OoO0O00 / OoOoOO00 * iIii1I11I1II1 . I1Ii111
 iIIiIi1iIII1 = getCurrPlayerInventory ( currentState )
 Ooooo = iIIiIi1iIII1 . getAnthill ( )
 if ( getAntAt ( currentState , Ooooo . coords ) == None ) :
  for type in range ( 1 , len ( UNIT_STATS ) ) :
   i1IiIi1i = UNIT_STATS [ type ] [ COST ]
   if ( i1IiIi1i <= iIIiIi1iIII1 . foodCount ) :
    OOOO0oo0 . append ( Move ( BUILD , [ Ooooo . coords ] , type ) )
    if 43 - 43: OOooOOo
 return OOOO0oo0
 if 57 - 57: O0 / o0oOOo0O0Ooo
 if 12 - 12: OoooooooOO / O0 + II111iiii * I1ii11iIi11i
 if 46 - 46: II111iiii - IiII * OoooooooOO / oO0o % IiII
 if 11 - 11: iIii1I11I1II1 . OoOoOO00 / IiII % ooOoO0o
 if 61 - 61: ooOoO0o - OOooOOo + OOooOOo
 if 40 - 40: i11iIiiIii . iIii1I11I1II1
 if 2 - 2: i1IIi * oO0o - oO0o + OoooooooOO % OoOoOO00 / OoOoOO00
 if 3 - 3: OoooooooOO
 if 71 - 71: IiII + i1IIi - iII111i - i11iIiiIii . I11i - ooOoO0o
 if 85 - 85: I1ii11iIi11i - OoOoOO00 / I1ii11iIi11i + OOooOOo - iII111i
 if 49 - 49: OoO0O00 - O0 / OoO0O00 * OoOoOO00 + I1Ii111
 if 35 - 35: II111iiii . I1IiiI / i1IIi / I1IiiI * oO0o
 if 85 - 85: II111iiii . ooOoO0o % OOooOOo % I11i
def OOo00ooOoO0o ( path ) :
 for O0OOo in path :
  if ( O0OOo [ 1 ] == BOARD_LENGTH / 2 - 1 ) or ( O0OOo [ 1 ] == BOARD_LENGTH / 2 ) :
   if 21 - 21: i11iIiiIii
   return False
 return True
 if 89 - 89: iII111i . i11iIiiIii * O0
 if 44 - 44: i1IIi . I1IiiI / i11iIiiIii + IiII
 if 27 - 27: OOooOOo
 if 52 - 52: I1Ii111 % OoOoOO00 + iIii1I11I1II1 * oO0o . Ii1I
 if 95 - 95: iIii1I11I1II1 . IiII - OoooooooOO * OoO0O00 / o0oOOo0O0Ooo
 if 74 - 74: oO0o
 if 34 - 34: iII111i
 if 44 - 44: i1IIi % I1IiiI % o0oOOo0O0Ooo
 if 9 - 9: Oo0Ooo % OoooooooOO - Ii1I
 if 43 - 43: OoO0O00 % OoO0O00
 if 46 - 46: Oo0Ooo % iIii1I11I1II1 . iII111i . O0 * ooOoO0o / OoooooooOO
def II1iI1IIi ( currentState ) :
 OOOO0oo0 = [ ]
 if 41 - 41: I1IiiI - I1Ii111 % II111iiii . I1Ii111 - I11i
 if 45 - 45: Ii1I - OOooOOo
 iIIiIi1iIII1 = getCurrPlayerInventory ( currentState )
 for i11 in iIIiIi1iIII1 . ants :
  if 70 - 70: OoO0O00 % I1IiiI / I1IiiI . I11i % ooOoO0o . II111iiii
  if ( i11 . hasMoved ) : continue
  if 10 - 10: Ii1I - i11iIiiIii . I1ii11iIi11i % i1IIi
  if 78 - 78: iIii1I11I1II1 * Oo0Ooo . Oo0Ooo - OOooOOo . iIii1I11I1II1
  I111I1I = listAllMovementPaths ( currentState ,
 i11 . coords ,
 UNIT_STATS [ i11 . type ] [ MOVEMENT ] ,
 UNIT_STATS [ i11 . type ] [ IGNORES_GRASS ] )
  if 54 - 54: II111iiii + I11i % I11i % o0oOOo0O0Ooo
  if 25 - 25: iII111i - Oo0Ooo
  if ( i11 . type == QUEEN ) :
   Iii1IIIIIII = [ ]
   for Oo0o0000o0o0 in I111I1I :
    if ( isPathOkForQueen ( Oo0o0000o0o0 ) ) :
     Iii1IIIIIII . append ( Oo0o0000o0o0 )
   I111I1I = Iii1IIIIIII
   if 27 - 27: OoO0O00 + OoOoOO00 * ooOoO0o
   if 83 - 83: iIii1I11I1II1
  for Oo0o0000o0o0 in I111I1I :
   OOOO0oo0 . append ( Move ( MOVE_ANT , Oo0o0000o0o0 , None ) )
   if 72 - 72: I11i
 return OOOO0oo0
 if 87 - 87: i1IIi
 if 48 - 48: Oo0Ooo * oO0o * iIii1I11I1II1 + i11iIiiIii - OoooooooOO
 if 38 - 38: OoOoOO00 / iIii1I11I1II1 % i11iIiiIii - IiII * iII111i / OoOoOO00
 if 13 - 13: OoO0O00 * I1ii11iIi11i - I1Ii111
 if 79 - 79: oO0o % o0oOOo0O0Ooo % OoOoOO00
 if 45 - 45: I1IiiI * OOooOOo % OoO0O00
 if 24 - 24: ooOoO0o - I11i * oO0o
 if 87 - 87: Ii1I - I1ii11iIi11i % I1ii11iIi11i . oO0o / I1ii11iIi11i
 if 6 - 6: OoOoOO00 / iIii1I11I1II1 * OoooooooOO * i11iIiiIii
 if 79 - 79: IiII % OoO0O00
 if 81 - 81: i11iIiiIii + i11iIiiIii * OoO0O00 + IiII
 if 32 - 32: O0 . OoooooooOO
def iiI ( currentState ) :
 OOOO0oo0 = [ ]
 OOOO0oo0 . extend ( listAllMovementMoves ( currentState ) )
 OOOO0oo0 . extend ( listAllBuildMoves ( currentState ) )
 OOOO0oo0 . append ( Move ( END , None , None ) )
 return OOOO0oo0
 if 17 - 17: i11iIiiIii / Oo0Ooo . OoO0O00 / I1IiiI
 if 38 - 38: i1IIi . I1ii11iIi11i % Ii1I + iIii1I11I1II1 + O0
 if 47 - 47: OoO0O00 + IiII / II111iiii
 if 97 - 97: I1ii11iIi11i / I1IiiI % O0 + i1IIi - ooOoO0o
 if 38 - 38: o0oOOo0O0Ooo % I1Ii111 + i11iIiiIii + iII111i + ooOoO0o / i11iIiiIii
def o0OOOOOo0 ( currentState ) :
 if 57 - 57: iIii1I11I1II1 + iIii1I11I1II1
 oO0o0Oo = None
 for oOoO in currentState . inventories :
  if oOoO . player == currentState . whoseTurn :
   oO0o0Oo = oOoO
   break
   if 76 - 76: ooOoO0o / OoOoOO00 + I1ii11iIi11i
 return oO0o0Oo
 if 2 - 2: i11iIiiIii - I1Ii111 + OoO0O00 % I11i * Ii1I
 if 54 - 54: O0 - iII111i . OOooOOo % iII111i + iII111i
 if 36 - 36: OOooOOo % i11iIiiIii
def Iiii1Ii ( currentState ) :
 if 62 - 62: i1IIi % OoOoOO00
 OOO0ooo = None
 for oOoO in currentState . inventories :
  if oOoO . player == currentState . whoseTurn :
   OOO0ooo = oOoO . getQueen ( )
   break
 return OOO0ooo
 if 37 - 37: I11i * i1IIi
 if 20 - 20: IiII + OoOoOO00 - OOooOOo - OOooOOo - I1ii11iIi11i
 if 7 - 7: O0
 if 26 - 26: o0oOOo0O0Ooo / OoooooooOO % ooOoO0o % OOooOOo
def oO0O0o0O ( self , currentState ) :
 i1Ii = getConstrList ( currentState , 2 , ( FOOD , ) )
 oOO00ooOOo = [ ]
 if ( currentState . inventories [ 0 ] . player == currentState . whoseTurn ) :
  oOO00ooOOo . append ( i1Ii [ 2 ] )
  oOO00ooOOo . append ( i1Ii [ 3 ] )
 else :
  oOO00ooOOo . append ( i1Ii [ 0 ] )
  oOO00ooOOo . append ( i1Ii [ 1 ] )
 return oOO00ooOOo
 if 20 - 20: I1ii11iIi11i
 if 3 - 3: OoO0O00 * i1IIi . I1IiiI . O0 - OoOoOO00
 if 81 - 81: I1IiiI - iIii1I11I1II1 / I1IiiI / O0
 if 34 - 34: Ii1I * Ii1I - I1ii11iIi11i - O0 . i11iIiiIii
 if 32 - 32: iIii1I11I1II1 . OoO0O00 * oO0o / OOooOOo . II111iiii - Oo0Ooo
def IIIi ( self , currentState ) :
 if ( currentState . inventories [ 0 ] . player == currentState . whoseTurn ) :
  return currentState . inventories [ 1 ]
 else :
  return currentState . inventories [ 0 ]
  if 39 - 39: oO0o * I1Ii111 + OoOoOO00 % OoooooooOO / iIii1I11I1II1
  if 60 - 60: Ii1I
  if 20 - 20: II111iiii - I11i + i1IIi + Ii1I
  if 7 - 7: ooOoO0o + Ii1I
  if 32 - 32: iIii1I11I1II1 % I1IiiI / i11iIiiIii + OOooOOo - o0oOOo0O0Ooo . iII111i
  if 86 - 86: i1IIi / Ii1I * I1IiiI
  if 67 - 67: I1ii11iIi11i * I1ii11iIi11i / oO0o * OoooooooOO + OoOoOO00
  if 79 - 79: i1IIi
  if 1 - 1: oO0o / i1IIi
  if 74 - 74: I11i / OoooooooOO / Oo0Ooo * i11iIiiIii . II111iiii . OoooooooOO
  if 59 - 59: i11iIiiIii . OoooooooOO / I11i * I1ii11iIi11i + OoooooooOO
  if 3 - 3: i11iIiiIii * Oo0Ooo % iIii1I11I1II1 % I1IiiI * iII111i / OOooOOo
  if 95 - 95: IiII * O0 * I1Ii111 . OoooooooOO % Oo0Ooo + I1ii11iIi11i
  if 98 - 98: oO0o . OoooooooOO
  if 54 - 54: O0 / IiII % ooOoO0o * i1IIi * O0
  if 48 - 48: o0oOOo0O0Ooo . oO0o % OoOoOO00 - OoOoOO00
  if 33 - 33: I11i % II111iiii + OoO0O00
  if 93 - 93: i1IIi . IiII / I1IiiI + IiII
  if 58 - 58: I1ii11iIi11i + O0 . Oo0Ooo + OoOoOO00 - OoO0O00 - OoOoOO00
  if 41 - 41: Oo0Ooo / i1IIi / Oo0Ooo - iII111i . o0oOOo0O0Ooo
  if 65 - 65: O0 * i11iIiiIii . OoooooooOO / I1IiiI / iII111i
def o00000oo00 ( currentState , move ) :
 if 41 - 41: OOooOOo - o0oOOo0O0Ooo + Ii1I
 i1II = currentState . fastclone ( )
 iIIiIi1iIII1 = getCurrPlayerInventory ( i1II )
 Ooo = i1II . whoseTurn
 IiIiII1 = iIIiIi1iIII1 . ants
 OO0oo00oOO = iIIiIi1iIII1 . getTunnels ( )
 i1III = iIIiIi1iIII1 . getAnthill ( )
 if 38 - 38: I1Ii111 . iII111i . I1IiiI * OoO0O00
 if 69 - 69: o0oOOo0O0Ooo % i11iIiiIii / Ii1I
 i11 = getAntAt ( i1II , i1III . coords )
 if i11 is not None :
  if i11 . player != Ooo :
   i1III . captureHealth -= 1
   if 93 - 93: ooOoO0o
   if 34 - 34: oO0o - ooOoO0o * Oo0Ooo / o0oOOo0O0Ooo
 iI1iiIi1 = [ WORKER , DRONE , SOLDIER , R_SOLDIER ]
 if move . moveType == BUILD :
  if move . buildType in iI1iiIi1 :
   i11 = Ant ( iIIiIi1iIII1 . getAnthill ( ) . coords , move . buildType , Ooo )
   iIIiIi1iIII1 . ants . append ( i11 )
   if 49 - 49: ooOoO0o . II111iiii
   if move . buildType == WORKER :
    iIIiIi1iIII1 . foodCount -= 1
   elif move . buildType == DRONE or move . buildType == R_SOLDIER :
    iIIiIi1iIII1 . foodCount -= 2
   elif move . buildType == SOLDIER :
    iIIiIi1iIII1 . foodCount -= 3
    if 24 - 24: O0 . OoooooooOO - OoO0O00 * OoooooooOO
  elif move . buildType == TUNNEL :
   print ( "Attempted tunnel build in getNextState()" )
   return currentState
   if 12 - 12: O0 + IiII * i1IIi . OoO0O00
   if 71 - 71: I1Ii111 - o0oOOo0O0Ooo - OOooOOo
 elif move . moveType == MOVE_ANT :
  iiIO0OO0o0O00oO = move . coordList [ - 1 ]
  o00O = move . coordList [ 0 ]
  for i11 in IiIiII1 :
   if i11 . coords == o00O :
    i11 . coords = iiIO0OO0o0O00oO
    if 92 - 92: Oo0Ooo - I1Ii111
    i11 . hasMoved = False
    if 24 - 24: oO0o / I1Ii111 / I11i % OoOoOO00 / I1ii11iIi11i * ooOoO0o
    if i11 . carrying and i11 . coords == iIIiIi1iIII1 . getAnthill ( ) . coords :
     iIIiIi1iIII1 . foodCount += 1
     i11 . carrying = False
    for iiIiIIi11I1 in OO0oo00oOO :
     if i11 . carrying and ( i11 . coords == iiIiIIi11I1 . coords ) :
      iIIiIi1iIII1 . foodCount += 1
      i11 . carrying = False
      if 86 - 86: iIii1I11I1II1 . I1IiiI * I11i
    if not i11 . carrying and i11 . type == WORKER :
     iI1Iii = getConstrList ( i1II , 2 , [ FOOD ] )
     for i1Ii in iI1Iii :
      if i1Ii . coords == i11 . coords :
       i11 . carrying = True
       if 49 - 49: o0oOOo0O0Ooo
    I11iiI = listAttackable ( i11 . coords , UNIT_STATS [ i11 . type ] [ RANGE ] )
    for O0OOo in I11iiI :
     i1iIii1i111 = getAntAt ( i1II , O0OOo )
     if i1iIii1i111 is not None :
      if i1iIii1i111 . player != Ooo :
       i1iIii1i111 . health = i1iIii1i111 . health - UNIT_STATS [ i11 . type ] [ ATTACK ]
       if 65 - 65: Oo0Ooo * O0 / Ii1I . I1Ii111 % Oo0Ooo
       if 24 - 24: OoO0O00
       if i1iIii1i111 . health <= 0 :
        i1II . inventories [ 1 - Ooo ] . ants . remove ( i1iIii1i111 )
        if 99 - 99: OOooOOo / IiII / Ii1I
       break
 return i1II
 if 84 - 84: OoO0O00 / iIii1I11I1II1
 if 33 - 33: i1IIi / I1Ii111 - i1IIi . Oo0Ooo
 if 18 - 18: Oo0Ooo / O0 + iII111i
 if 65 - 65: i1IIi . I1ii11iIi11i / ooOoO0o
 if 11 - 11: IiII * ooOoO0o / ooOoO0o - OOooOOo
 if 68 - 68: I1IiiI % IiII - IiII / I1IiiI + I1ii11iIi11i - Oo0Ooo
 if 65 - 65: ooOoO0o - i1IIi
 if 62 - 62: I11i / oO0o % Oo0Ooo . OoooooooOO / i11iIiiIii / I1Ii111
 if 60 - 60: I1IiiI % oO0o / o0oOOo0O0Ooo % oO0o * i11iIiiIii / iII111i
 if 34 - 34: I1Ii111 - OOooOOo
 if 25 - 25: oO0o % I1IiiI + i11iIiiIii + O0 * OoooooooOO
 if 64 - 64: i1IIi
 if 10 - 10: I1Ii111 % O0 / I1IiiI % I11i
def iiII ( currentState , move ) :
 if 28 - 28: ooOoO0o . OoooooooOO + o0oOOo0O0Ooo + Ii1I % iII111i
 o000Oo = getNextState ( currentState , move )
 iIIiIi1iIII1 = getCurrPlayerInventory ( o000Oo )
 IiIiII1 = iIIiIi1iIII1 . ants
 if 73 - 73: OoOoOO00 + Oo0Ooo
 if 61 - 61: iIii1I11I1II1
 if move . moveType == MOVE_ANT :
  o00O = move . coordList [ 0 ]
  for i11 in IiIiII1 :
   if i11 . coords == o00O :
    i11 . hasMoved = True
 elif move . moveType == END :
  for i11 in IiIiII1 :
   i11 . hasMoved = False
  o000Oo . whoseTurn = 1 - currentState . whoseTurn
 return o000Oo
 if 47 - 47: OoooooooOO
 if 2 - 2: OoOoOO00 % I1Ii111 * Oo0Ooo * OoOoOO00
 if 65 - 65: i11iIiiIii + Oo0Ooo * OoooooooOO - OoO0O00
 if 26 - 26: o0oOOo0O0Ooo % OOooOOo + OOooOOo % I11i * i11iIiiIii / iII111i
 if 64 - 64: oO0o % OoOoOO00 / II111iiii % ooOoO0o - iII111i
def I1II1IiI1 ( ant ) :
 if ( ant == None ) :
  return " "
 elif ( ant . type == QUEEN ) :
  return "Q"
 elif ( ant . type == WORKER ) :
  return "W"
 elif ( ant . type == DRONE ) :
  return "D"
 elif ( ant . type == SOLDIER ) :
  return "S"
 elif ( ant . type == R_SOLDIER ) :
  return "I"
 else :
  return "?"
  if 26 - 26: OOooOOo * Oo0Ooo
  if 31 - 31: I11i * oO0o . Ii1I
  if 35 - 35: I11i
  if 94 - 94: ooOoO0o / i11iIiiIii % O0
def O0oO0oo0O ( constr ) :
 if ( constr == None ) :
  return " "
 if ( constr . type == ANTHILL ) :
  return "^"
 elif ( constr . type == TUNNEL ) :
  return "@"
 elif ( constr . type == GRASS ) :
  return ";"
 elif ( constr . type == FOOD ) :
  return "%"
 else :
  return "?"
  if 82 - 82: OoooooooOO . Ii1I
  if 26 - 26: oO0o + IiII - II111iiii . II111iiii + I1ii11iIi11i + OoOoOO00
  if 68 - 68: O0
  if 76 - 76: I1ii11iIi11i
def ooO000OO ( loc ) :
 if ( loc == None ) :
  return " "
 elif ( loc . ant != None ) :
  return charRepAnt ( loc . ant )
 elif ( loc . constr != None ) :
  return charRepConstr ( loc . constr )
 else :
  return "."
  if 43 - 43: ooOoO0o * I1Ii111 % OOooOOo
  if 38 - 38: Oo0Ooo
  if 34 - 34: OoOoOO00
  if 70 - 70: iIii1I11I1II1 * IiII - OOooOOo / Oo0Ooo % oO0o
  if 66 - 66: OoooooooOO + ooOoO0o * iII111i
  if 2 - 2: iII111i . OoO0O00 / oO0o
  if 41 - 41: OoO0O00 . I1Ii111 * IiII * I1Ii111
  if 74 - 74: iIii1I11I1II1 / o0oOOo0O0Ooo
  if 58 - 58: iIii1I11I1II1 - I1IiiI % o0oOOo0O0Ooo % OoooooooOO * iIii1I11I1II1 + OOooOOo
  if 25 - 25: OOooOOo % O0
  if 44 - 44: I1Ii111 . Ii1I * II111iiii / IiII + iIii1I11I1II1
def Ii1111III1 ( state ) :
 if 74 - 74: I1ii11iIi11i - iII111i * i1IIi
 if 12 - 12: O0
 OoO00OooO0 = list ( range ( 0 , 10 ) )
 o00OOo = " 0123456789"
 if ( state . whoseTurn == PLAYER_TWO ) :
  OoO00OooO0 = list ( range ( 9 , - 1 , - 1 ) )
  o00OOo = " 9876543210"
  if 40 - 40: iIii1I11I1II1 + iII111i * OoOoOO00 + oO0o
  if 15 - 15: I11i % I1IiiI - iIii1I11I1II1 * ooOoO0o
 print ( o00OOo )
 oO0O0o0o000 = 0
 for ii111I in OoO00OooO0 :
  III1 = str ( ii111I )
  for Oo0ooo0Ooo in OoO00OooO0 :
   i11 = getAntAt ( state , ( Oo0ooo0Ooo , ii111I ) )
   if ( i11 != None ) :
    III1 += charRepAnt ( i11 )
   else :
    i11i1i1I1iI1 = getConstrAt ( state , ( Oo0ooo0Ooo , ii111I ) )
    if ( i11i1i1I1iI1 != None ) :
     III1 += charRepConstr ( i11i1i1I1iI1 )
    else :
     III1 += "."
  print ( III1 + str ( ii111I ) )
  oO0O0o0o000 += 1
 print ( o00OOo )
 if 66 - 66: o0oOOo0O0Ooo * OOooOOo + Ii1I * o0oOOo0O0Ooo + OOooOOo / OoooooooOO
 if 86 - 86: Ii1I . iII111i - iII111i
 oo0 = state . inventories [ 0 ] . foodCount
 i11i = state . inventories [ 1 ] . foodCount
 print ( " food: " + str ( oo0 ) + "/" + str ( i11i ) )
 if 73 - 73: ooOoO0o % ooOoO0o . iII111i + I1Ii111
 if 10 - 10: O0 / OOooOOo * ooOoO0o - OoO0O00 - i1IIi . OoOoOO00
class OO00O00Oo :
 if 66 - 66: O0 . OOooOOo + o0oOOo0O0Ooo
 def xyz__init__ ( self , parent = None , coords = None , f = 0.0 , g = 0.0 , h = 0.0 ) :
  self . parent = parent
  self . coords = coords
  self . f = f
  self . g = g
  self . h = h
  if 3 - 3: II111iiii - Ii1I % OoOoOO00 / oO0o
 def xyz__hash__ ( self ) :
  return hash ( self . coords )
  if 44 - 44: O0 . Ii1I * iII111i / i11iIiiIii
 def xyz__eq__ ( self , other ) :
  if self . coords == other . coords :
   return True
  return False
  if 56 - 56: OoOoOO00 % I1ii11iIi11i - Ii1I % iIii1I11I1II1
 def xyz__str__ ( self ) :
  return str ( self . coords )
  if 76 - 76: OoooooooOO * OoooooooOO - iII111i - iIii1I11I1II1 . OoooooooOO / I1ii11iIi11i
  if 86 - 86: ooOoO0o
  if 51 - 51: OoO0O00 - i11iIiiIii * I1IiiI
  if 95 - 95: OOooOOo % I1ii11iIi11i + o0oOOo0O0Ooo % ooOoO0o
  if 36 - 36: O0 / i1IIi % II111iiii / iII111i
  if 96 - 96: Oo0Ooo / oO0o . II111iiii . Oo0Ooo
  if 91 - 91: II111iiii . OOooOOo + o0oOOo0O0Ooo
  if 8 - 8: OOooOOo * Oo0Ooo / iII111i - OoO0O00 - OoooooooOO
  if 100 - 100: oO0o . iIii1I11I1II1 . iIii1I11I1II1
  if 55 - 55: oO0o
  if 37 - 37: IiII / i11iIiiIii / Oo0Ooo
def o0ooOO00OO0o0O ( currentState , start , goal ) :
 start = OO00O00Oo ( coords = start )
 goal = OO00O00Oo ( coords = goal )
 if 35 - 35: o0oOOo0O0Ooo * iII111i - iIii1I11I1II1 + o0oOOo0O0Ooo . OoooooooOO
 i11 = getAntAt ( currentState , start . coords )
 if 13 - 13: O0 % ooOoO0o % I11i
 Ii11IiI111 = UNIT_STATS [ i11 . type ] [ MOVEMENT ]
 Ii11IiI111 = Ii11IiI111 + 1
 if 31 - 31: OoO0O00 * O0 / I11i . OoooooooOO * I11i . I1ii11iIi11i
 if start . coords == goal . coords :
  return [ ]
  if 50 - 50: OoO0O00 * I11i - o0oOOo0O0Ooo + IiII * OoO0O00 % oO0o
 start . f = start . g + approxDist ( start . coords , goal . coords )
 O00o0000OO = [ start , ]
 O0Ooo0O0OO = list ( )
 iiI1iiii1Iii = start
 if 94 - 94: i11iIiiIii % oO0o + Oo0Ooo + oO0o
 while O00o0000OO :
  if iiI1iiii1Iii == goal :
   return construct_path ( iiI1iiii1Iii , Ii11IiI111 )
   if 33 - 33: IiII . Oo0Ooo / iIii1I11I1II1
  iiI1iiii1Iii = O00o0000OO . pop ( O00o0000OO . index ( min ( O00o0000OO , key = lambda ii111I : ii111I . f ) ) )
  if 50 - 50: o0oOOo0O0Ooo
  if iiI1iiii1Iii in O0Ooo0O0OO :
   continue
   if 16 - 16: OoOoOO00
  for IIiI in neighbors ( currentState , iiI1iiii1Iii , goal ) :
   if IIiI == goal :
    return construct_path ( iiI1iiii1Iii , Ii11IiI111 )
   if IIiI in O00o0000OO :
    II1 = next ( ( x for x in O00o0000OO if x . coords == IIiI . coords ) , None )
    if next ( ( x for x in O00o0000OO if x . coords == IIiI . coords ) , None ) is not None :
     if II1 . f < IIiI . f :
      continue
   if IIiI in O0Ooo0O0OO :
    II1 = next ( ( x for x in O00o0000OO if x . coords == IIiI . coords ) , None )
    if next ( ( x for x in O00o0000OO if x . coords == IIiI . coords ) , None ) is not None :
     if II1 . f < IIiI . f :
      continue
     else :
      O00o0000OO . append ( IIiI )
    else :
     O00o0000OO . append ( IIiI )
   else :
    O00o0000OO . append ( IIiI )
    if 17 - 17: Oo0Ooo + OoooooooOO * OoooooooOO
  O0Ooo0O0OO . append ( iiI1iiii1Iii )
  if 5 - 5: I1Ii111 % OoooooooOO . OoOoOO00
 return False
 if 67 - 67: I1ii11iIi11i + Ii1I
 if 72 - 72: IiII % o0oOOo0O0Ooo
def OooooO ( currentState , node , goal ) :
 oO00OoO0oo = [ OO00O00Oo ( coords = Oo0ooo0Ooo ) for Oo0ooo0Ooo in listReachAdj ( currentState , node . coords , goal . coords ) ]
 for o00o0o000Oo in oO00OoO0oo :
  o00o0o000Oo . g = node . g + 1
  o00o0o000Oo . f = o00o0o000Oo . g + approxDist ( o00o0o000Oo . coords , goal . coords )
  o00o0o000Oo . parent = node
 return oO00OoO0oo
 if 100 - 100: i1IIi - i11iIiiIii . I1Ii111 * OoO0O00
 if 62 - 62: O0
def iiIIIIiii ( node , antMovement ) :
 Oo0o0000o0o0 = [ node , ]
 iiii1 = list ( )
 while node . parent is not None :
  node = node . parent
  Oo0o0000o0o0 . append ( node )
  if 22 - 22: iIii1I11I1II1 * I1Ii111 / Oo0Ooo
 for ii111I in Oo0o0000o0o0 :
  iiii1 . append ( ii111I . coords )
  if 31 - 31: i11iIiiIii
 O0O0O = iiii1 [ : : - 1 ]
 if 38 - 38: Oo0Ooo / iIii1I11I1II1 * iIii1I11I1II1 % I1ii11iIi11i
 return O0O0O if len ( O0O0O ) <= antMovement else O0O0O [ : antMovement ]
 if 92 - 92: I11i / O0 * I1IiiI - I11i
 if 99 - 99: i11iIiiIii % OoooooooOO
def o0000O00oO0O ( state , coords , givenAntCoords ) :
 if 3 - 3: iIii1I11I1II1 % I1ii11iIi11i . OOooOOo % I11i
 O00OooO = listAdjacent ( coords )
 if 40 - 40: ooOoO0o * Ii1I . Ii1I + II111iiii + OoooooooOO
 if 17 - 17: IiII % Ii1I
 iiii = [ ]
 for I11I1i1iI in O00OooO :
  i11 = getAntAt ( state , I11I1i1iI )
  if 46 - 46: I1IiiI - I11i / OoooooooOO - i1IIi . i11iIiiIii
  if i11 is None :
   iiii . append ( I11I1i1iI )
  elif i11 . coords is givenAntCoords :
   iiii . append ( I11I1i1iI )
   if 15 - 15: II111iiii * oO0o % iII111i / i11iIiiIii - oO0o + Oo0Ooo
 return iiii
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
