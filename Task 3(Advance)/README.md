# Cricket Fielding Analysis Project

This project implements a detailed fielding performance analysis system for T20 cricket matches. It allows tracking and analyzing the fielding performance of players, helping teams make data-driven decisions for strategic fielding placements.

## Features

- Track detailed fielding events for multiple players
- Calculate comprehensive performance metrics
- Generate analysis reports in CSV format
- Support for various fielding actions and outcomes

## Data Collection Features

The system tracks the following parameters for each fielding event:
- Match No.
- Innings
- Team
- Player Name
- Ballcount
- Position
- Short Description
- Pick (clean pick/good throw/fumble/bad throw/catch/drop catch)
- Throw (run out/missed stumping/missed run out/stumping)
- Runs (saved/conceded)
- Overcount
- Venue

## Performance Metrics

The system calculates a Performance Score (PS) using the following formula:
```
PS = (CP×WCP) + (GT×WGT) + (C×WC) + (DC×WDC) + (ST×WST) + (RO×WRO) + (MRO×WMRO) + (DH×WDH) + RS
```

Where:
- CP: Clean Picks
- GT: Good Throws
- C: Catches
- DC: Dropped Catches
- ST: Stumpings
- RO: Run Outs
- MRO: Missed Run Outs
- DH: Direct Hits
- RS: Runs Saved
- W**: Respective weights for each metric

## Usage

1. Run the script `Q1.py`
2. Add fielding events using the `add_fielding_event()` method
3. The script will automatically:
   - Process the data
   - Calculate performance metrics
   - Generate CSV files with raw data and analysis

## Output Files

The script generates two types of CSV files in the `fielding_analysis` directory:
1. `fielding_data_[timestamp].csv`: Raw fielding event data
2. `fielding_analysis_[timestamp].csv`: Analyzed performance metrics for each player

## Requirements

- Python 3.x
- pandas library

## Getting Started

1. Ensure you have Python installed
2. Install required packages: `pip install pandas`
3. Run the script: `python Q1.py`
4. Check the `fielding_analysis` directory for results

## Sample Data

The script includes sample data to demonstrate its functionality. You can modify the `main()` function to add your own match data.

Example:
```python
analysis.add_fielding_event(
    match_no=1,
    innings=1,
    team='Team A',
    player_name='Player 1',
    ballcount=1,
    position='Mid-off',
    description='Clean pick and throw',
    pick='clean pick',
    throw='good throw',
    runs=1,
    overcount=1,
    venue='Stadium X'
)
```
