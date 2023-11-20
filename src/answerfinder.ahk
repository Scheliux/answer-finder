#Include, lib/json.ahk

CoordMode, ToolTip, Screen
FileEncoding, UTF-8

FileSelectFile, Filename, 3, ./, Open a file, JSON File (*.json)
if (Filename = "") {
    MsgBox, , AntiAltTab, No file was selected.
}

FileRead, jsonString, %Filename%
Data := JSON.Load(jsonString)

Shift::
    Answer := ""

    for i in Data {
        if (InStr(Data[i].q, Clipboard)) {
            if (Answer = "") {
                Answer := Data[i].a
            } else {
                Answer .= "`n`n" Data[i].a
            }
        }
    }

    if (Answer = "") {
        Answer := "Answer not found :("
    }

    ToolTip, %Answer%, 0, 0
    SetTimer, RemoveToolTip, -5000

    Return

RemoveToolTip:
    ToolTip
    Return

F5::
    Reload

Esc::
    ExitApp