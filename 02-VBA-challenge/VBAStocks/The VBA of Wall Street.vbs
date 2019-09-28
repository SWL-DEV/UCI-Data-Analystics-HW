Sub testing():

    For Each ws In Worksheets
    
        'Create headers'
        ws.Range("I1").Value = "Tickers"
        ws.Range("J1").Value = "Yearly Change"
        ws.Range("K1").Value = "Percent Change"
        ws.Range("L1").Value = "Total Stock Volume"
        ws.Range("O2").Value = "Greatest % Increase"
        ws.Range("O3").Value = "Greatest % Decrease"
        ws.Range("O4").Value = "Greatest Total Volume"
        ws.Range("P1").Value = "Ticker"
        ws.Range("Q1").Value = "Value"
        
        Worksheets("A").Columns("I:Q").AutoFit
        
        
        Dim symbol As String
        Dim TotalVol As Double
        TotalVol = 0
        Dim SumTable As Long
        SumTable = 2
        Dim YearOpen As Double
        Dim YearEnd As Double
        Dim YearlyChange As Double
        Dim PercentChange As Double
        Dim StartRow As Long
        StartRow = 2
        Dim LastRow As Long
                
        'Find last row of the data set'
        LastRow = ws.Cells(Rows.Count, "A").End(xlUp).Row
        
             
    For I = 2 To LastRow
        
            TotalVol = TotalVol + Cells(I, 7).Value
        
            
            If ws.Cells(I + 1, 1).Value <> ws.Cells(I, 1).Value Then
                    
                symbol = ws.Cells(I, 1).Value
            

                ws.Range("I" & SumTable).Value = symbol
            
            
                ws.Range("L" & SumTable).Value = TotalVol
            
                
                TotalVol = 0
                
                           
            
           
                'Opening number of a ticker'
                YearOpen = ws.Range("C" & StartRow)
            
                'Closing number of a ticker'
                YearEnd = ws.Range("F" & I)
            
                YearlyChange = YearEnd - YearOpen
                
                ws.Range("J" & SumTable).Value = YearlyChange
            
                'Find Percent Change'
                If YearOpen = 0 Then
            
                    PercentChange = 0
                
                Else
                    YearOpen = ws.Range("C" & StartRow)
                    
                    PercentChange = YearlyChange / YearOpen
                
                              
                End If
        
        
                ws.Range("K" & SumTable).NumberFormat = "0.00%"
                ws.Range("K" & SumTable).Value = PercentChange
                
                
                If ws.Range("J" & SumTable).Value >= 0 Then
                
                    ws.Range("J" & SumTable).Interior.ColorIndex = 4
            
                Else
                
                    ws.Range("J" & SumTable).Interior.ColorIndex = 3
            
                
                End If
                

                SumTable = SumTable + 1
                
                StartRow = I + 1
                
            End If
               
        Next I
        
        
        Dim PercentChangeCol As Range
        Dim MaxIncrease As Double
        Dim MaxDecrease As Double
        Dim MaxIncRow As Long
        Dim MaxDecRow As Long
        Dim TotalStockVol As Range
        Dim MaxTotalVol As LongLong
        Dim MaxTotalVolRow As Long
        Dim SumTableLastRow As Long
        
        SumTableLastRow = ws.Cells(Rows.Count, "K").End(xlUp).Row
        
        Set PercentChangeCol = ws.Range("K:K")
        
            'Find maximum and minimum in the Percent Change column'
            MaxIncrease = Application.WorksheetFunction.Max(PercentChangeCol)
            ws.Range("Q2").Value = MaxIncrease
            
            MaxDecrease = Application.WorksheetFunction.Min(PercentChangeCol)
            ws.Range("Q3").Value = MaxDecrease
            
            ws.Range("Q2: Q3").NumberFormat = "0.00%"
            
            
            'Finding the ticker symbol that matches the max % increase and decrease'
            For a = 2 To SumTableLastRow
            
                If ws.Cells(a, "K").Value = MaxIncrease Then
                
                    MaxIncRow = a
                    
                    ws.Range("P2").Value = ws.Range("I" & a).Value
                
                End If
            
            
            Next a
            
            For b = 2 To SumTableLastRow
            
                If ws.Cells(b, "K").Value = MaxDecrease Then
                
                    MaxDecRow = a
                    
                    ws.Range("P3").Value = ws.Range("I" & b).Value
                
                End If
                  
    
            Next b
            
            
            'Finding Greatest Total Volume'
            Set TotalStockVol = ws.Range("L:L")
            
                MaxTotalVol = Application.WorksheetFunction.Max(TotalStockVol)
                
                ws.Range("Q4").Value = MaxTotalVol
                
                
                For c = 2 To SumTableLastRow
                
                    If ws.Cells(c, "L").Value = MaxTotalVol Then
                    
                        MaxTotalVolRow = c
                        
                        ws.Range("P4").Value = ws.Range("I" & c).Value
                        
                    End If
                
                Next c
                              
  
        
    Next ws

End Sub
