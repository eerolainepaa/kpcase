# RoomLight - Instructions

## Overview

RoomLight is a command-line interface (CLI) prototype that simulates a smart hotel room lighting system. This prototype demonstrates proximity-based lighting control for different user types (guests and staff) and various room areas.

## Features

- **User Management**: Set user type (guest or staff)
- **Room Access**: Enter/leave room with automatic lighting
- **Area Control**: Navigate between room areas with smart lighting
- **Mood Settings**: Apply different lighting moods (relax, working, wakeup)
- **Maintenance Dashboard**: Monitor light status and detect faults
- **Fault Simulation**: Test system with simulated light failures

## Getting Started

### Prerequisites

- Python 3.x installed on your system

### Running the Prototype

1. Navigate to the RoomLight directory:

2. Run the prototype:
   `python RoomLight.py`

3. The CLI will start and display available commands.

## Available Commands

### Basic Commands

| Command | Description | Example |
|---------|-------------|---------|
| `help` | Show all available commands | `help` |
| `quit` | Exit the prototype | `quit` |

### User Management

| Command | Description | Example |
|---------|-------------|---------|
| `user <type>` | Set user type (staff/guest) | `user guest` |

### Room Control

| Command | Description | Example |
|---------|-------------|---------|
| `enter` | Enter the room (lights turn on based on user type) | `enter` |
| `leave` | Leave the room (all lights turn off) | `leave` |

### Area Navigation

| Command | Description | Example |
|---------|-------------|---------|
| `enter <area>` | Enter a specific room area | `enter bathroom` |

**Available areas:**
- `bathroom`
- `bed`
- `entrance`
- `desk`
- `living_room`

### Lighting Moods

| Command | Description | Example |
|---------|-------------|---------|
| `mood <type>` | Set lighting mood for current area | `mood relax` |

**Available moods:**
- `relax` - 30% brightness (comfortable lighting)
- `working` - 80% brightness (bright for tasks)
- `wakeup` - 50% brightness (gentle morning light)

### Maintenance & Testing

| Command | Description | Example |
|---------|-------------|---------|
| `dashboard` | Show maintenance dashboard with light status | `dashboard` |
| `reset` | Reset room to default state | `reset` |
| `break <area>` | Simulate a light fault in specified area | `break bathroom` |

## Usage Examples

### Guest Scenario

```
Command: user guest
User has been set: guest

Command: enter
Guest entered room. Turn entrance ON

Command: enter bathroom
Entered area: bathroom: light ON, brightness 100%

Command: mood relax
Room mood has been set to: relax

Command: leave
Room is empty, turning all lights off
```

### Staff Scenario

```
Command: user staff
User has been set: staff

Command: enter
Staff entered, turn all lights on (100%)

Command: dashboard

=== MAINTENANCE DASHBOARD ===
 - living_room | Status: ON      | Brightness: 100%
 - bed         | Status: ON      | Brightness: 100%
 - desk        | Status: ON      | Brightness: 100%
 - entrance    | Status: ON      | Brightness: 100%
 - bathroom    | Status: ON      | Brightness: 100%
=============================
```

### Fault Simulation

```
Command: break bathroom
Light has broken in area: bathroom

Command: dashboard

=== MAINTENANCE DASHBOARD ===
 - living_room | Status: ON      | Brightness: 100%
 - bed         | Status: ON      | Brightness: 100%
 - desk        | Status: ON      | Brightness: 100%
 - entrance    | Status: ON      | Brightness: 100%
 - bathroom    | Status: FAULTY  | Brightness: 0%
=============================
```

## System Behavior

### Guest Behavior
- When entering room: Only entrance light turns on
- When entering areas: Previous area light turns off, new area light turns on
- Moods apply to current area only

### Staff Behavior
- When entering room: All lights turn on at 100% brightness
- Staff have access to all areas simultaneously

### Lighting Logic
- Lights automatically turn off when leaving areas
- Faulty lights cannot be turned on until reset
- Moods override default brightness levels
- Reset command restores all lights to operational state

## Troubleshooting

### Common Issues

1. **"Error, Set user first"**
   - Solution: Use `user guest` or `user staff` before entering the room

2. **"ERROR Unknown error"**
   - Solution: Check command spelling or use `help` for available commands

3. **"ERROR give user/area/mood"**
   - Solution: Provide the required parameter (e.g., `user guest`, `enter bathroom`)

### Resetting the System

If the system gets into an unexpected state:
```
Command: reset
Room has been reseted to default
```

This clears all user settings, areas, and moods, and turns off all lights.

## Project Context

This prototype is part of a Software Production & Architecture course project for Kempower. It demonstrates key requirements including:

- Proximity-based lighting for housekeeping and guests
- Mood-based lighting settings
- Maintenance dashboard for fault monitoring
- Automatic light control when rooms are empty

## Technical Notes

- Built with Python 3.x
- Uses object-oriented design with Light and Room classes
- Command-line interface for easy testing and demonstration
