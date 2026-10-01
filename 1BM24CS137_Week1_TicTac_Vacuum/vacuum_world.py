def reflex_vacuum_agent(current_room, room_A_state, room_B_state):
    if current_room == 'A':
        if room_A_state == 'dirty':
            return 'clean'
        else:
            return 'move_right'
    elif current_room == 'B':
        if room_B_state == 'dirty':
            return 'clean'
        else:
            return 'move_left'
    return 'no_action'


current_room = 'A'
room_A_state = 'dirty'
room_B_state = 'dirty'

print("Initial State:")
print(f"  Current Room: {current_room}")
print(f"  Room A: {room_A_state}")
print(f"  Room B: {room_B_state}")
print("---------------------")

for step in range(1, 10):
    action = reflex_vacuum_agent(current_room, room_A_state, room_B_state)
    print(f"Step {step}: Agent in {current_room}, A: {room_A_state}, B: {room_B_state} -> Action: {action}")

    if action == 'clean':
        if current_room == 'A':
            room_A_state = 'clean'
        elif current_room == 'B':
            room_B_state = 'clean'
    elif action == 'move_right':
        current_room = 'B'
    elif action == 'move_left':
        current_room = 'A'

    if room_A_state == 'clean' and room_B_state == 'clean':
        print("All rooms are clean! Agent can rest.")
        if current_room == 'A':
            break

print("\nFinal State:")
print(f"  Current Room: {current_room}")
print(f"  Room A: {room_A_state}")
print(f"  Room B: {room_B_state}")
