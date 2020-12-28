#Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
#Por exemplo, o programa deve converter 14:25 em 2:25 P.M.
#A entrada é dada em dois inteiros.
#Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída.
#Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim,
#a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M.
#Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que
#desejar
# resumindo <-  conversor de sistema 24h pra 12h am ou pm :)

def conversão(horas, minutos):
        if horas > 12:
                AMorPM = 'PM'
                horario_convertido = horas - 12
        if horas < 12:
                AMorPM = 'AM'
                horario_convertido = horas
        if horas == 12 and minutos == 00:
                print('são meio dia!!')
                return
        if horas == 00 and minutos == 00:
                print('são meia noite !! vai  dormir vagabundo')
                return
        print('no sistema 12h, são {}:{} {}'.format(horario_convertido,minutos,AMorPM))

a = str(input('Voce quer escrever um horario (sistema 24h!)? [S/N] ')).strip().lower()
while a == 's':
        p_horas = int(input('digite a hora: '))
        p_minutos = int(input('digite os minutos: '))
        conversão(p_horas,p_minutos)
        a = str(input('Voce quer escrever outro horário? [S/N] ')).strip().lower()
if a == 'n':
        exit()