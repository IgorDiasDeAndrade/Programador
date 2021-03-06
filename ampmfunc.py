def add_time(start, duration, dia = ''):
    novotempo = ''

    temp = []

    #temp = [str.split(':') for str in start.split(' ')]
    for sta in start.split(' '):
        temp.append(sta.split(':'))

    inicioHora, inicioMinuto = temp[0]
    periodo=' '.join(temp[1])


    #[start_hours, start_mins, period] = [*temp[0], *temp[1]]
    horaAdicionada, minutoAdicionado = duration.split(':')

    dias = 0
    horas = int(inicioHora) + int(horaAdicionada)
    minutos = int(inicioMinuto) + int(minutoAdicionado)

    if periodo == 'PM':
        horas += 12
    else:
        horas += 0

    horas += minutos // 60
    minutos = minutos % 60

    dias = horas // 24
    horas = horas % 24

    if horas > 11:
        periodo = 'PM'
    else:
        periodo = 'AM'

    if horas > 12:
        horas -= 12
    else:
        horas += 0

    if horas == 0:
        horas = 12
    else:
        horas


    novotempo += str(horas).format()
    novotempo += ':'
    novotempo += str(minutos).zfill(2)
    novotempo += ' ' + periodo

    mensagem = ''

    if len(dia) != 0:
        semana = [
        'Sunday', 'Monday', 'Tuesday',
            'Wednesday', 'Thursday', 'Friday',
            'Saturday', 'Sunday', 'Monday',
            'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday'
            ]
        if dias > 7:
            i = dias % 7
        else:
            i = dias
        indice = semana.index(dia.capitalize())
        mensagem += ', ' + semana[indice + i]

    if dias == 0:
        mensagem += ''
    elif dias == 1:
        mensagem += ' (next day)'
    else:
        mensagem += ' (' + str(dias) + ' days later)'

    novotempo += mensagem
    print(novotempo)
    return novotempo

add_time("09:00 AM","32:00", "Wednesday")
                                                                                                                                                                                                
