Attribute VB_Name = "YearlyChanges"
' Iterates the data in the spreadsheet
' calculates the price change, percent change
' and total stock volume for the ticker symbol
Sub yearlyChange()
    Dim tstartRow As Long
        ' per Microsoft Documentation this code
        ' may be necessary for data types to handle
        ' data overflow errors (Double seems to fix it)
        ' tstartRow = CLng(2000) * 365
    Dim tendRow As Long
    Dim data As Variant
    Dim diff As Double
    
    ' Developer note: the data should be sorted before removing duplicates
    ' It is assumed this data is sorted
    With ActiveSheet
        ' Finds the last cell in the column
        lastrow = .Range("J2").End(xlDown).Address
        ' Create a data array of stock symbols
        data = .Range("J2:" + lastrow).Value
        ' Iterate the array of stock symbols and create the report
        For i = 1 To UBound(data)
            ' ticker symbol
            ticker = data(i, 1)
            ' ticker start row
            tstartRow = .Range("A:A").Find(What:=ticker, After:=.Range("A1"), LookAt:=xlWhole).row
            ' ticker end row
            tendRow = .Range("A:A").Find(What:=ticker, After:=.Range("A1"), searchdirection:=xlPrevious, LookAt:=xlWhole).row
            ' ticker opening amount
            open_amt = Cells(tstartRow, 3)
            ' ticker closing amount
            close_amt = Cells(tendRow, 6)
            ' price difference
            diff = close_amt - open_amt
            ' percent change
            pct_change = diff / open_amt
            Cells(i + 1, 11).Value = diff
            Cells(i + 1, 12).Value = pct_change
            
            ' Call custom sub to format the percent change cells
            Call formatPctChange(diff, i + 1, 11)
            ' Call custom function to calculate the total stock volume for each ticker
            Cells(i + 1, 13).Value = calcStockVolume(tstartRow, tendRow)
            ' Format stock volume column to not use scientific notation
            ' This is necessary for the MaxMinTotals module
            .Range("M:M").NumberFormat = "0"
        Next
        
    End With
End Sub
' Calculates the total stock volume for each stock
Function calcStockVolume(startrow As Long, endrow As Long) As Double
    Dim stockvol As Double
    stockvol = 0
    ' Iterate stock data for each stock and calc the total stock volume
    For i = startrow To endrow
        stockvol = stockvol + Cells(i, 7).Value
    Next i
    ' Return total stock volume
    calcStockVolume = stockvol
End Function
' Formats the percent change cell fill for each stock
Sub formatPctChange(diff As Double, r As Long, c As Long)
    If diff > 0 Then
        ' apply green (positive percent change)
        Cells(r, c).Interior.ColorIndex = 4
    ElseIf diff < 0 Then
        ' apply red (negative percent change)
        Cells(r, c).Interior.ColorIndex = 3
    Else
        ' apply yellow (no change)
        Cells(r, c).Interior.ColorIndex = 6
    End If
End Sub


