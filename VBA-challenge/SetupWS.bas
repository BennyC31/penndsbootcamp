Attribute VB_Name = "SetupWS"
' Initializes the spreadsheet
Sub formatReportInfo()
' Adds the header columns/rows to the spreadsheet
    With ActiveSheet
        Cells(1, 10).Value = "Ticker"
        Cells(1, 11).Value = "Yearly Change"
        Cells(1, 12).Value = "Percent Change"
        Cells(1, 13).Value = "Total Stock Volume"
        Cells(1, 17).Value = "Ticker"
        Cells(1, 18).Value = "Value"
        Cells(2, 16).Value = "Greatest % Increase"
        Cells(3, 16).Value = "Greatest % Decrease"
        Cells(4, 16).Value = "Greatest Total Volume"
        ' Formats the Percent change column
        .Range("L:L").NumberFormat = "0.00%"
             
    End With
End Sub
' Clears the report headers and data
Sub clearReport()
    With ActiveSheet
        .Range("J:R").Value = ""
        .Range("K:K").Interior.ColorIndex = 0
    End With
End Sub
' Auto fits the columns for readability
Sub autoFit()
    ActiveSheet.Range("A:R").Columns.autoFit
End Sub

