import pandas as pd
from datetime import datetime
import os

class FieldingAnalysis:
    def __init__(self):
        self.data = []
        self.weights = {
            'WCP': 1,  # Weight for Clean Picks
            'WGT': 1,  # Weight for Good Throws
            'WC': 1,   # Weight for Catches
            'WDC': -1, # Weight for Dropped Catches
            'WST': 1,  # Weight for Stumpings
            'WRO': 1,  # Weight for Run Outs
            'WMRO': -1,# Weight for Missed Run Outs
            'WDH': 1   # Weight for Direct Hits
        }
    
    def add_fielding_event(self, match_no, innings, team, player_name, ballcount, 
                          position, description, pick, throw, runs, overcount, venue):
        """Add a fielding event to the dataset"""
        event = {
            'Match_No': match_no,
            'Innings': innings,
            'Team': team,
            'Player_Name': player_name,
            'Ballcount': ballcount,
            'Position': position,
            'Short_Description': description,
            'Pick': pick,
            'Throw': throw,
            'Runs': runs,
            'Overcount': overcount,
            'Venue': venue
        }
        self.data.append(event)

    def calculate_performance_score(self, player_data):
        """Calculate performance score for a player using the given formula"""
        metrics = {
            'CP': sum(1 for event in player_data if event['Pick'] == 'clean pick'),
            'GT': sum(1 for event in player_data if event['Pick'] == 'good throw'),
            'C': sum(1 for event in player_data if event['Pick'] == 'catch'),
            'DC': sum(1 for event in player_data if event['Pick'] == 'drop catch'),
            'ST': sum(1 for event in player_data if event['Throw'] == 'stumping'),
            'RO': sum(1 for event in player_data if event['Throw'] == 'run out'),
            'MRO': sum(1 for event in player_data if event['Throw'] == 'missed run out'),
            'DH': sum(1 for event in player_data if event['Pick'] == 'direct hit'),
            'RS': sum(event['Runs'] for event in player_data)  # Sum of runs saved/conceded
        }
        
        ps = (
            metrics['CP'] * self.weights['WCP'] +
            metrics['GT'] * self.weights['WGT'] +
            metrics['C'] * self.weights['WC'] +
            metrics['DC'] * self.weights['WDC'] +
            metrics['ST'] * self.weights['WST'] +
            metrics['RO'] * self.weights['WRO'] +
            metrics['MRO'] * self.weights['WMRO'] +
            metrics['DH'] * self.weights['WDH'] +
            metrics['RS']
        )
        
        return ps, metrics

    def analyze_players(self):
        """Analyze performance for all players in the dataset"""
        df = pd.DataFrame(self.data)
        players = df['Player_Name'].unique()
        analysis_results = []

        for player in players:
            player_data = [event for event in self.data if event['Player_Name'] == player]
            performance_score, metrics = self.calculate_performance_score(player_data)
            
            result = {
                'Player': player,
                'Performance_Score': performance_score,
                'Total_Events': len(player_data),
                **metrics
            }
            analysis_results.append(result)

        return pd.DataFrame(analysis_results)

    def export_to_csv(self, output_dir='fielding_analysis'):
        """Export raw data and analysis to CSV files"""
        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Export raw data
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        raw_data_file = f'{output_dir}/fielding_data_{timestamp}.csv'
        pd.DataFrame(self.data).to_csv(raw_data_file, index=False)

        # Export analysis
        analysis_file = f'{output_dir}/fielding_analysis_{timestamp}.csv'
        analysis_df = self.analyze_players()
        analysis_df.to_csv(analysis_file, index=False)

        return raw_data_file, analysis_file

def main():
    # Create an instance of FieldingAnalysis
    analysis = FieldingAnalysis()

    # Example: Add sample fielding events
    # You can modify these values or add more events as needed
    analysis.add_fielding_event(
        match_no=1,
        innings=1,
        team='Team A',
        player_name='John Doe',
        ballcount=1,
        position='Mid-off',
        description='Clean pick and throw to keeper',
        pick='clean pick',
        throw='good throw',
        runs=1,
        overcount=1,
        venue='Stadium X'
    )

    # Add more events here...

    # Export the data and analysis
    raw_data_file, analysis_file = analysis.export_to_csv()
    
    print(f"Raw data exported to: {raw_data_file}")
    print(f"Analysis exported to: {analysis_file}")
    
    # Display analysis
    analysis_df = analysis.analyze_players()
    print("\nFielding Analysis Summary:")
    print(analysis_df)

if __name__ == "__main__":
    main()
