def vacuum_world():
    # Initializing goal state, where 0 indicates Clean and 1 indicates Dirty
    goal_state = {'A': '0', 'B': '0'}
    cost = 0

    # User input for vacuum location and room statuses
    location_input = input("Enter Location of Vacuum (A/B): ").upper()  # User input for vacuum's location (A or B)
    status_input = input(f"Enter status of {location_input} (1 for Dirty, 0 for Clean): ")  # Status of the current room
    status_input_complement = input(f"Enter status of the other room (1 for Dirty, 0 for Clean): ")  # Status of the other room

    # Display initial condition
    print("\nInitial Location Condition: " + str(goal_state))

    # Vacuum is placed in Location A
    if location_input == 'A':
        print("Vacuum is placed in Location A")

        # If Location A is Dirty
        if status_input == '1':
            print("Location A is Dirty.")
            # Clean Location A
            goal_state['A'] = '0'
            cost += 1  # Cost for sucking dirt
            print("Cost for CLEANING A: " + str(cost))
            print("Location A has been Cleaned.")

            # Check status of Location B
            if status_input_complement == '1':  # If Location B is Dirty
                print("Location B is Dirty.")
                print("Moving right to Location B.")
                cost += 1  # Cost for moving right
                print("Cost for MOVING RIGHT: " + str(cost))

                # Clean Location B
                goal_state['B'] = '0'
                cost += 1  # Cost for sucking dirt
                print("Cost for SUCK: " + str(cost))
                print("Location B has been Cleaned.")
            else:
                print("Location B is already clean. No action. Cost: " + str(cost))

        # If Location A is already clean
        else:
            print("Location A is already clean.")
            # Check status of Location B
            if status_input_complement == '1':  # If Location B is Dirty
                print("Location B is Dirty.")
                print("Moving RIGHT to Location B.")
                cost += 1  # Cost for moving right
                print("Cost for MOVING RIGHT: " + str(cost))

                # Clean Location B
                goal_state['B'] = '0'
                cost += 1  # Cost for sucking dirt
                print("Cost for SUCK: " + str(cost))
                print("Location B has been Cleaned.")
            else:
                print("Location B is already clean. No action. Cost: " + str(cost))

    # Vacuum is placed in Location B
    else:
        print("Vacuum is placed in Location B")

        # If Location B is Dirty
        if status_input == '1':
            print("Location B is Dirty.")
            # Clean Location B
            goal_state['B'] = '0'
            cost += 1  # Cost for sucking dirt
            print("Cost for CLEANING B: " + str(cost))
            print("Location B has been Cleaned.")

            # Check status of Location A
            if status_input_complement == '1':  # If Location A is Dirty
                print("Location A is Dirty.")
                print("Moving LEFT to Location A.")
                cost += 1  # Cost for moving left
                print("Cost for MOVING LEFT: " + str(cost))

                # Clean Location A
                goal_state['A'] = '0'
                cost += 1  # Cost for sucking dirt
                print("Cost for SUCK: " + str(cost))
                print("Location A has been Cleaned.")
            else:
                print("Location A is already clean. No action. Cost: " + str(cost))

        # If Location B is already clean
        else:
            print("Location B is already clean.")
            # Check status of Location A
            if status_input_complement == '1':  # If Location A is Dirty
                print("Location A is Dirty.")
                print("Moving LEFT to Location A.")
                cost += 1  # Cost for moving left
                print("Cost for MOVING LEFT: " + str(cost))

                # Clean Location A
                goal_state['A'] = '0'
                cost += 1  # Cost for sucking dirt
                print("Cost for SUCK: " + str(cost))
                print("Location A has been Cleaned.")
            else:
                print("Location A is already clean. No action. Cost: " + str(cost))

    # Final Goal State and Performance Measurement
    print("\nGOAL STATE: ")
    print(goal_state)
    print("Performance Measurement (Total Cost): " + str(cost))


# Running the vacuum world
vacuum_world()
