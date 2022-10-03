Attribute VB_Name = "Main"
' Main Module used to call methods to create
' the report
Sub runAll()
    ' Clears all generated data
    Call SetupWS.clearReport
    ' Creates and formats report columns
    Call SetupWS.formatReportInfo
    ' Gets all stock ticker symbols
    Call StockTicker.get_unique
    ' Produces the yearly changes for each stock
    Call YearlyChanges.yearlyChange
    ' Gets the stock highlights based on all stocks
    Call MaxMinTotals.callAll
    ' Auto fits the columns in the worksheet
    Call SetupWS.autoFit
End Sub
