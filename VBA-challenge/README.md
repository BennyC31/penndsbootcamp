# Overview
The vba files run on the active sheet.  The macro files were created on a Mac so each spreadsheet contains the same command buttons that call the same common code.
###### Note: Some research was done to create a form and have one set of command buttons for the workbook.  As it turns out, this is not recommended because there is no form designer for the Mac.

## VBA Files
**Main.bas**: Run All (macro button)

Calls all sub procedures and functions to create the output.

**SetupWS.bas**: Reset (macro button), Setup (macro button) and Auto Fit (macro button)
* Reset clears the report output.
* Setup Creates the column headers and formats the report columns.
* Auto fits the worksheet columns.

**StockTicker.bas**: Stock List (macro button)

Gets all distinct stock ticker symbols.

**YearlyChanges.bas**: Yearly Change (macro button)

Calculates the yearly changes for each stock.

**MaxMinTotals.bas**: Min/Max/Total Volume (macro button)

Gets the stock highlights based on all stocks.

## Recommended Steps
1. Click Run All
2. Click Auto Fit
## Alternate Steps
1. Click Reset
2. Click Setup
3. Click Stock List
4. Click Yearly Change
5. Click Min/Max/Total Volume
6. Click Auto Fit

## General Notes
Each spreadsheet takes between 40 minutes to 1 hour and 30 minutes to finish.

## Developer Notes
There are plenty of opportunity to refactor the code.  There are a few areas where code is being duplicated and can be moved to a common method for reusability.  For this iteration, it is more important to get the files to run and produce the correct results.

There may be an opportunity for performance improvements by calling the yearly changes and percent changes separate from the Total Stock Volume.  The for loop within the for loop for the Total Stock Volume is more than likely the biggest performance hit.
