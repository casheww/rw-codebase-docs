*Namespace : none*
## LizardAI
**Base class** : ArtificialIntelligence


**Methods** :
<details>
<summary><code>ctor(AbstractCreature, World)</code>
</summary>

**Parameters** :
  - **creature** (`AbstractCreature`)
  - **world** (`World`)

**Returns** : `System.Void`

</details><details>
<summary><code>ModuleToTrackRelationship(CreatureTemplate.Relationship)</code>
</summary>

**Parameters** :
  - **relationship** (`CreatureTemplate/Relationship`)

**Returns** : `AIModule`

</details><details>
<summary><code>CreateTrackedCreatureState(RelationshipTracker.DynamicRelationship)</code>
</summary>

**Parameters** :
  - **rel** (`RelationshipTracker/DynamicRelationship`)

**Returns** : `RelationshipTracker/TrackedCreatureState`

</details><details>
<summary><code>UpdateDynamicRelationship(RelationshipTracker.DynamicRelationship)</code>
</summary>

**Parameters** :
  - **dRelation** (`RelationshipTracker/DynamicRelationship`)

**Returns** : `CreatureTemplate/Relationship`

</details><details>
<summary><code>get_lizard()</code>
</summary>

**Parameters** :


**Returns** : `Lizard`

</details><details>
<summary><code>get_CombinedFear()</code>
</summary>

**Parameters** :


**Returns** : `System.Single`

</details><details>
<summary><code>NewRoom(Room)</code>
</summary>

**Parameters** :
  - **room** (`Room`)

**Returns** : `System.Void`

</details><details>
<summary><code>DetermineBehavior()</code>
</summary>

**Parameters** :


**Returns** : `LizardAI/Behavior`

</details><details>
<summary><code>get_TravelUtility()</code>
</summary>

**Parameters** :


**Returns** : `System.Single`

</details><details>
<summary><code>get_RoomLike()</code>
</summary>

**Parameters** :


**Returns** : `System.Single`

</details><details>
<summary><code>Update()</code>
</summary>

**Parameters** :


**Returns** : `System.Void`

</details><details>
<summary><code>NewArea(System.Boolean)</code>
</summary>

**Parameters** :
  - **strandedFromExits** (`System.Boolean`)

**Returns** : `System.Void`

</details><details>
<summary><code>WantToStayInDenUntilEndOfCycle()</code>
</summary>

**Parameters** :


**Returns** : `System.Boolean`

</details><details>
<summary><code>VisualScore(UnityEngine.Vector2, System.Single)</code>
</summary>

**Parameters** :
  - **lookAtPoint** (`UnityEngine.Vector2`)
  - **bonus** (`System.Single`)

**Returns** : `System.Single`

</details><details>
<summary><code>AggressiveBehavior(Tracker.CreatureRepresentation, System.Single)</code>
</summary>

**Parameters** :
  - **target** (`Tracker/CreatureRepresentation`)
  - **tongueChance** (`System.Single`)

**Returns** : `System.Void`

</details><details>
<summary><code>UnpleasantFallRisk(RWCustom.IntVector2)</code>
</summary>

**Parameters** :
  - **tile** (`RWCustom.IntVector2`)

**Returns** : `System.Boolean`

</details><details>
<summary><code>FallRisk(RWCustom.IntVector2)</code>
</summary>

**Parameters** :
  - **tile** (`RWCustom.IntVector2`)

**Returns** : `System.Boolean`

</details><details>
<summary><code>BitCreature(BodyChunk)</code>
</summary>

**Parameters** :
  - **chunk** (`BodyChunk`)

**Returns** : `System.Void`

</details><details>
<summary><code>CreatureSpotted(System.Boolean, Tracker.CreatureRepresentation)</code>
</summary>

**Parameters** :
  - **firstSpot** (`System.Boolean`)
  - **otherCreature** (`Tracker/CreatureRepresentation`)

**Returns** : `System.Void`

</details><details>
<summary><code>CreateTrackerRepresentationForCreature(AbstractCreature)</code>
</summary>

**Parameters** :
  - **otherCreature** (`AbstractCreature`)

**Returns** : `Tracker/CreatureRepresentation`

</details><details>
<summary><code>LikeOfPlayer(Tracker.CreatureRepresentation)</code>
</summary>

**Parameters** :
  - **player** (`Tracker/CreatureRepresentation`)

**Returns** : `System.Single`

</details><details>
<summary><code>CurrentPlayerAggression(AbstractCreature)</code>
</summary>

**Parameters** :
  - **player** (`AbstractCreature`)

**Returns** : `System.Single`

</details><details>
<summary><code>TravelPreference(MovementConnection, PathCost)</code>
</summary>

**Parameters** :
  - **connection** (`MovementConnection`)
  - **cost** (`PathCost`)

**Returns** : `PathCost`

</details><details>
<summary><code>IdleSpotScore(WorldCoordinate)</code>
</summary>

**Parameters** :
  - **coord** (`WorldCoordinate`)

**Returns** : `System.Single`

</details><details>
<summary><code>ComfortableIdlePosition()</code>
</summary>

**Parameters** :


**Returns** : `System.Boolean`

</details><details>
<summary><code>DoIWantToHoldThisWithMyTongue(BodyChunk)</code>
</summary>

**Parameters** :
  - **chunk** (`BodyChunk`)

**Returns** : `System.Boolean`

</details><details>
<summary><code>DoIWantToBiteThisCreature(Tracker.CreatureRepresentation)</code>
</summary>

**Parameters** :
  - **otherCrit** (`Tracker/CreatureRepresentation`)

**Returns** : `System.Boolean`

</details><details>
<summary><code>SendCommunication(Lizard, LizardAI.LizardCommunication)</code>
</summary>

**Parameters** :
  - **otherLizard** (`Lizard`)
  - **signal** (`LizardAI/LizardCommunication`)

**Returns** : `System.Void`

</details><details>
<summary><code>RecieveCommunication(Lizard, LizardAI.LizardCommunication)</code>
</summary>

**Parameters** :
  - **otherLizard** (`Lizard`)
  - **signal** (`LizardAI/LizardCommunication`)

**Returns** : `System.Void`

</details><details>
<summary><code>ReactToNoise(NoiseTracker.TheorizedSource, Noise.InGameNoise)</code>
</summary>

**Parameters** :
  - **source** (`NoiseTracker/TheorizedSource`)
  - **noise** (`Noise.InGameNoise`)

**Returns** : `System.Void`

</details><details>
<summary><code>SocialEvent(SocialEventRecognizer.EventID, Creature, Creature, PhysicalObject)</code>
</summary>

**Parameters** :
  - **ID** (`SocialEventRecognizer/EventID`)
  - **subjectCrit** (`Creature`)
  - **objectCrit** (`Creature`)
  - **involvedItem** (`PhysicalObject`)

**Returns** : `System.Void`

</details><details>
<summary><code>LizardPlayerRelationChange(System.Single, AbstractCreature)</code>
</summary>

**Parameters** :
  - **change** (`System.Single`)
  - **player** (`AbstractCreature`)

**Returns** : `System.Void`

</details><details>
<summary><code>GiftRecieved(SocialEventRecognizer.OwnedItemOnGround)</code>
</summary>

**Parameters** :
  - **giftOfferedToMe** (`SocialEventRecognizer/OwnedItemOnGround`)

**Returns** : `System.Void`

</details>

**Properties** : 
<details>
<summary><code>lizard</code>
</summary>

`{ get; }`

**Type** : Lizard
</details><details>
<summary><code>CombinedFear</code>
</summary>

`{ get; }`

**Type** : System.Single
</details><details>
<summary><code>TravelUtility</code>
</summary>

`{ get; }`

**Type** : System.Single
</details><details>
<summary><code>RoomLike</code>
</summary>

`{ get; }`

**Type** : System.Single
</details>

**Fields** : 
<details>
<summary><code>excitement</code>
</summary>

**Type** : System.Single
</details><details>
<summary><code>panic</code>
</summary>

**Type** : System.Int32
</details><details>
<summary><code>hunger</code>
</summary>

**Type** : System.Single
</details><details>
<summary><code>fear</code>
</summary>

**Type** : System.Single
</details><details>
<summary><code>rainFear</code>
</summary>

**Type** : System.Single
</details><details>
<summary><code>lastDistressLength</code>
</summary>

**Type** : System.Int32
</details><details>
<summary><code>runSpeed</code>
</summary>

**Type** : System.Single
</details><details>
<summary><code>currentUtility</code>
</summary>

**Type** : System.Single
</details><details>
<summary><code>idleCounter</code>
</summary>

**Type** : System.Int32
</details><details>
<summary><code>idleSpotWinStreak</code>
</summary>

**Type** : System.Int32
</details><details>
<summary><code>forbiddenIdleSpot</code>
</summary>

**Type** : WorldCoordinate
</details><details>
<summary><code>idleRestlessness</code>
</summary>

**Type** : System.Int32
</details><details>
<summary><code>unableToFindComfortablePosition</code>
</summary>

**Type** : System.Int32
</details><details>
<summary><code>focusCreature</code>
</summary>

**Type** : Tracker/CreatureRepresentation
</details><details>
<summary><code>timeInRoom</code>
</summary>

**Type** : System.Int32
</details><details>
<summary><code>casualAggressionTarget</code>
</summary>

**Type** : Tracker/CreatureRepresentation
</details><details>
<summary><code>submittedTo</code>
</summary>

**Type** : AbstractCreature
</details><details>
<summary><code>attemptBiteFrames</code>
</summary>

**Type** : System.Int32
</details><details>
<summary><code>yellowAI</code>
</summary>

**Type** : YellowAI
</details><details>
<summary><code>redSpitAI</code>
</summary>

**Type** : LizardAI/LizardSpitTracker
</details><details>
<summary><code>dbspr</code>
</summary>

**Type** : DebugSprite
</details><details>
<summary><code>dbspr2</code>
</summary>

**Type** : DebugSprite
</details><details>
<summary><code>debugDestinationVisualizer</code>
</summary>

**Type** : DebugDestinationVisualizer
</details><details>
<summary><code>lurkTracker</code>
</summary>

**Type** : LizardAI/LurkTracker
</details><details>
<summary><code>usedToVultureMask</code>
</summary>

**Type** : System.Int32
</details><details>
<summary><code>behavior</code>
</summary>

**Type** : LizardAI/Behavior
</details>

---

### Nested types

## LizardAI/Behavior
**Base class** : System.Enum

*sealed class*


**Methods** :


**Properties** : 


**Fields** : 
<details>
<summary><code>System.Int32 LizardAI/Behavior::value__</code>
</summary>

**Type** : System.Int32
</details><details>
<summary><code>staticLizardAI/Behavior LizardAI/Behavior::Idle</code>
</summary>

**Type** : LizardAI/Behavior
</details><details>
<summary><code>staticLizardAI/Behavior LizardAI/Behavior::Hunt</code>
</summary>

**Type** : LizardAI/Behavior
</details><details>
<summary><code>staticLizardAI/Behavior LizardAI/Behavior::Flee</code>
</summary>

**Type** : LizardAI/Behavior
</details><details>
<summary><code>staticLizardAI/Behavior LizardAI/Behavior::Travelling</code>
</summary>

**Type** : LizardAI/Behavior
</details><details>
<summary><code>staticLizardAI/Behavior LizardAI/Behavior::EscapeRain</code>
</summary>

**Type** : LizardAI/Behavior
</details><details>
<summary><code>staticLizardAI/Behavior LizardAI/Behavior::ReturnPrey</code>
</summary>

**Type** : LizardAI/Behavior
</details><details>
<summary><code>staticLizardAI/Behavior LizardAI/Behavior::Injured</code>
</summary>

**Type** : LizardAI/Behavior
</details><details>
<summary><code>staticLizardAI/Behavior LizardAI/Behavior::Fighting</code>
</summary>

**Type** : LizardAI/Behavior
</details><details>
<summary><code>staticLizardAI/Behavior LizardAI/Behavior::Frustrated</code>
</summary>

**Type** : LizardAI/Behavior
</details><details>
<summary><code>staticLizardAI/Behavior LizardAI/Behavior::ActingOutMission</code>
</summary>

**Type** : LizardAI/Behavior
</details><details>
<summary><code>staticLizardAI/Behavior LizardAI/Behavior::Lurk</code>
</summary>

**Type** : LizardAI/Behavior
</details><details>
<summary><code>staticLizardAI/Behavior LizardAI/Behavior::InvestigateSound</code>
</summary>

**Type** : LizardAI/Behavior
</details><details>
<summary><code>staticLizardAI/Behavior LizardAI/Behavior::GoToSpitPos</code>
</summary>

**Type** : LizardAI/Behavior
</details><details>
<summary><code>staticLizardAI/Behavior LizardAI/Behavior::FollowFriend</code>
</summary>

**Type** : LizardAI/Behavior
</details>

## LizardAI/LizardCommunication
**Base class** : System.Enum

*sealed class*


**Methods** :


**Properties** : 


**Fields** : 
<details>
<summary><code>System.Int32 LizardAI/LizardCommunication::value__</code>
</summary>

**Type** : System.Int32
</details><details>
<summary><code>staticLizardAI/LizardCommunication LizardAI/LizardCommunication::Agression</code>
</summary>

**Type** : LizardAI/LizardCommunication
</details><details>
<summary><code>staticLizardAI/LizardCommunication LizardAI/LizardCommunication::Submission</code>
</summary>

**Type** : LizardAI/LizardCommunication
</details>

## LizardAI/LizardTrackState
**Base class** : RelationshipTracker/TrackedCreatureState


**Methods** :
<details>
<summary><code>System.Void LizardAI/LizardTrackState::ctor()</code>
</summary>

**Parameters** :


**Returns** : `System.Void`

</details>

**Properties** : 


**Fields** : 
<details>
<summary><code>System.Boolean LizardAI/LizardTrackState::spear</code>
</summary>

**Type** : System.Boolean
</details><details>
<summary><code>System.Int32 LizardAI/LizardTrackState::vultureMask</code>
</summary>

**Type** : System.Int32
</details>

## LizardAI/LizardInjuryTracker
**Base class** : AIModule


**Methods** :
<details>
<summary><code>System.Void LizardAI/LizardInjuryTracker::ctor(ArtificialIntelligence, Lizard)</code>
</summary>

**Parameters** :
  - **AI** (`ArtificialIntelligence`)
  - **lizard** (`Lizard`)

**Returns** : `System.Void`

</details><details>
<summary><code>System.Single LizardAI/LizardInjuryTracker::Utility()</code>
</summary>

**Parameters** :


**Returns** : `System.Single`

</details>

**Properties** : 


**Fields** : 
<details>
<summary><code>Lizard LizardAI/LizardInjuryTracker::lizard</code>
</summary>

**Type** : Lizard
</details>

## LizardAI/LurkTracker
**Base class** : AIModule


**Methods** :
<details>
<summary><code>System.Void LizardAI/LurkTracker::ctor(ArtificialIntelligence, Lizard)</code>
</summary>

**Parameters** :
  - **AI** (`ArtificialIntelligence`)
  - **lizard** (`Lizard`)

**Returns** : `System.Void`

</details><details>
<summary><code>System.Void LizardAI/LurkTracker::Update()</code>
</summary>

**Parameters** :


**Returns** : `System.Void`

</details><details>
<summary><code>System.Single LizardAI/LurkTracker::LurkPosScore(WorldCoordinate)</code>
</summary>

**Parameters** :
  - **testLurkPos** (`WorldCoordinate`)

**Returns** : `System.Single`

</details><details>
<summary><code>System.Single LizardAI/LurkTracker::Utility()</code>
</summary>

**Parameters** :


**Returns** : `System.Single`

</details>

**Properties** : 


**Fields** : 
<details>
<summary><code>Lizard LizardAI/LurkTracker::lizard</code>
</summary>

**Type** : Lizard
</details><details>
<summary><code>WorldCoordinate LizardAI/LurkTracker::lurkPosition</code>
</summary>

**Type** : WorldCoordinate
</details><details>
<summary><code>RWCustom.IntVector2 LizardAI/LurkTracker::lookPosition</code>
</summary>

**Type** : RWCustom.IntVector2
</details><details>
<summary><code>System.Int32 LizardAI/LurkTracker::bestVisLook</code>
</summary>

**Type** : System.Int32
</details>

## LizardAI/LizardSpitTracker
**Base class** : AIModule


**Methods** :
<details>
<summary><code>System.Void LizardAI/LizardSpitTracker::ctor(ArtificialIntelligence)</code>
</summary>

**Parameters** :
  - **AI** (`ArtificialIntelligence`)

**Returns** : `System.Void`

</details><details>
<summary><code>LizardAI LizardAI/LizardSpitTracker::get_lizardAI()</code>
</summary>

**Parameters** :


**Returns** : `LizardAI`

</details><details>
<summary><code>System.Boolean LizardAI/LizardSpitTracker::get_AtSpitPos()</code>
</summary>

**Parameters** :


**Returns** : `System.Boolean`

</details><details>
<summary><code>System.Void LizardAI/LizardSpitTracker::Update()</code>
</summary>

**Parameters** :


**Returns** : `System.Void`

</details><details>
<summary><code>System.Nullable`1<UnityEngine.Vector2> LizardAI/LizardSpitTracker::AimPos()</code>
</summary>

**Parameters** :


**Returns** : `System.Nullable`1<UnityEngine.Vector2>`

</details><details>
<summary><code>System.Void LizardAI/LizardSpitTracker::AimABitUp(System.Single)</code>
</summary>

**Parameters** :
  - **am** (`System.Single`)

**Returns** : `System.Void`

</details><details>
<summary><code>System.Void LizardAI/LizardSpitTracker::AimABitDown(System.Single)</code>
</summary>

**Parameters** :
  - **am** (`System.Single`)

**Returns** : `System.Void`

</details><details>
<summary><code>System.Void LizardAI/LizardSpitTracker::SetAim(System.Single)</code>
</summary>

**Parameters** :
  - **am** (`System.Single`)

**Returns** : `System.Void`

</details><details>
<summary><code>System.Single LizardAI/LizardSpitTracker::SpitFromPosScore(WorldCoordinate)</code>
</summary>

**Parameters** :
  - **testPos** (`WorldCoordinate`)

**Returns** : `System.Single`

</details>

**Properties** : 
<details>
<summary><code>LizardAI LizardAI/LizardSpitTracker::lizardAI</code>
</summary>

`{ get; }`

**Type** : LizardAI
</details><details>
<summary><code>System.Boolean LizardAI/LizardSpitTracker::AtSpitPos</code>
</summary>

`{ get; }`

**Type** : System.Boolean
</details>

**Fields** : 
<details>
<summary><code>System.Boolean LizardAI/LizardSpitTracker::spitting</code>
</summary>

**Type** : System.Boolean
</details><details>
<summary><code>System.Boolean LizardAI/LizardSpitTracker::wantToSpit</code>
</summary>

**Type** : System.Boolean
</details><details>
<summary><code>System.Boolean LizardAI/LizardSpitTracker::targetReachable</code>
</summary>

**Type** : System.Boolean
</details><details>
<summary><code>WorldCoordinate LizardAI/LizardSpitTracker::wantToSpitAtPos</code>
</summary>

**Type** : WorldCoordinate
</details><details>
<summary><code>WorldCoordinate LizardAI/LizardSpitTracker::tempSpitFromPos</code>
</summary>

**Type** : WorldCoordinate
</details><details>
<summary><code>WorldCoordinate LizardAI/LizardSpitTracker::spitFromPos</code>
</summary>

**Type** : WorldCoordinate
</details><details>
<summary><code>System.Int32 LizardAI/LizardSpitTracker::randomCycle</code>
</summary>

**Type** : System.Int32
</details><details>
<summary><code>System.Int32 LizardAI/LizardSpitTracker::delay</code>
</summary>

**Type** : System.Int32
</details><details>
<summary><code>System.Int32 LizardAI/LizardSpitTracker::dontWannaSpitCounter</code>
</summary>

**Type** : System.Int32
</details><details>
<summary><code>System.Int32 LizardAI/LizardSpitTracker::wannaSpitCounter</code>
</summary>

**Type** : System.Int32
</details><details>
<summary><code>System.Int32 LizardAI/LizardSpitTracker::goToSpitPosCounter</code>
</summary>

**Type** : System.Int32
</details><details>
<summary><code>System.Single LizardAI/LizardSpitTracker::aimUp</code>
</summary>

**Type** : System.Single
</details><details>
<summary><code>System.Single LizardAI/LizardSpitTracker::generalAimUp</code>
</summary>

**Type** : System.Single
</details><details>
<summary><code>BodyChunk LizardAI/LizardSpitTracker::aimForChunk</code>
</summary>

**Type** : BodyChunk
</details>