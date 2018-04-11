import Resources.BaseResource as Resources

class BaseRace:
    resources = {Resources.Cylindar: 0,
                 Resources.Yellow: 0,
                 Resources.Black: 0,
                 Resources.Blue: 0,
                 Resources.Green: 0,
                 Resources.Brown: 0,
                 Resources.White: 0
                 }

    temporary_converters = []  # Converters traded from another player
    converters = []
    colonies = []
    research_teams = []
