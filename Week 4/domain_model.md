# Domain Model

### 1. Key Concepts
- Guest
- Wristband
- Room
- Light
- Sensor
- LightingSystem
- LightingMood
- MobileUI
- ControlPanel
- Receptionist
- Housekeeping
- Maintenance

### 2. Relationships
- Guest uses Wristband
- Wristband is assigned to Room
- Room contains Lights
- Room contains Sensors
- Sensor detects Wristband
- LightingSystem controls Lights
- LightingSystem receives data from Sensors
- LightingSystem applies LightingMood
- Guest uses MobileUI
- MobileUI controls LightingSystem
- Maintenance uses ControlPanel
- ControlPanel monitors LightingSystem
- Receptionist resets Room
- Housekeeping activates lights in Room

### Domain Model
```
  Guest ──uses──> Wristband ──assigned to──> Room
                                              │
                                              ├──contains──> Light
                                              ├──contains──> Sensor
                                              │
  Sensor ──detects──> Wristband

  LightingSystem ──controls──> Light
  LightingSystem ──receives data from──> Sensor
  LightingSystem ──applies──> LightingMood

  Guest ──uses──> MobileUI ──controls──> LightingSystem

  Maintenance ──uses──> ControlPanel ──monitors──> LightingSystem

  Receptionist ──resets──> Room
  Housekeeping ──activates lights in──> Room
```