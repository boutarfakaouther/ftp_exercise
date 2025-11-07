# Activity Planner System
# Simulates planning tasks over a day with decision-making
# and summary reporting

def compute_focus_level(hours_slept):
    if hours_slept < 0 or hours_slept > 24:
        return "invalid"
    elif hours_slept >= 8:
        focus = "High"
    elif hours_slept >= 5:
        focus = "Medium"
    else:
        focus == "Low"
    print("Focus level:", focus)


def select_tasks(focus_level):
    tasks = []
    if focus_level == "High":
        tasks.append("Deep Work")
        tasks.append("Team Sync")
        tasks.append("Creative Writing")
    elif focus_level == "Medium":
        tasks += "Emails", "Documentation"
    elif focus_level == "Low":
        tasks = ["Break", "Stretching", "Meditation"]
    else:
        print("Unknown focus level")
    return tasks


def estimate_durations(tasks):
    durations = {}
    for task in tasks:
        if task == "Deep Work":
            durations[task] = 180  # minutes
        elif task in ["Emails", "Documentation"]:
            durations[task] = 45
        elif task == "Team Sync":
            durations[task] = 30
        elif task == "Creative Writing":
            durations[task] = 60
        else:
            durations[task] = 15
    print("Estimated durations:", durations)
    return durations


def execute_schedule(durations):
    completed = []
    time_budget = 240  # 4 hours
    for task in durations:
        if durations[task] < time_budget:
            print("Executing:", task)
            time_budget -= durations[task]
            completed += task
        else:
            print("Skipping:", task, "- Not enough time")
    return completed


def summarize(completed_tasks, planned_tasks):
    print("Summary:")
    print("Planned:", planned_tasks)
    print("Completed:", completed_tasks)
    missed = set(planned_tasks) - set(completed_tasks)
    if len(missed) > 0:
        print("Missed:", missed)
    else:
        print("All tasks completed!")


def main():
    hours_slept = 6
    focus = compute_focus_level(hours_slept)

    tasks = select_tasks(focus)
    if len(tasks) == 0:
        print("No tasks selected. Exiting.")
        return

    estimate_durations(tasks)
    completed = execute_schedule(tasks)
    summarize(completed, tasks)


main()
