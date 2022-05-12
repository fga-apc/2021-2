#!/bin/sh
maestro-grades grade_exam checkio
maestro-grades grade_exam checkio-levels
maestro-grades grade_exam prova-1
maestro-grades grade_exam prova-2
maestro-grades grade_exam prova-3
maestro-grades grade_exam trabalho-final
maestro-grades collect --progress --output notas.xlsx
maestro-grades collect --by-grade --name --progress