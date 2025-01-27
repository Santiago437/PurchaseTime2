import flet as ft
import datetime




 
logo = ft.Image(src="logo.jpg" , width=100 , height=100)
container = ft.Container(bgcolor='blue',content= logo,
                             shape=ft.BoxShape.CIRCLE,clip_behavior=ft.ClipBehavior.ANTI_ALIAS, )
produto = ft.TextField(bgcolor="blue",border_radius=50,width=120)
fornecedor = ft.TextField(bgcolor="blue",border_radius=50,width=120)
frequencia = ft.TextField(bgcolor="blue",border_radius=50,width=120)
quantidade = ft.TextField(bgcolor="blue",border_radius=50,width=120)
texto_data_inicio = ft.Text("Data Inicio",bgcolor="blue",width=120)
cadastrar_pedido = ft.ElevatedButton("Cadastrar Pedido",bgcolor="blue",color="white")

def main(page):
    def change_date(e):
        print(f"Date picker changed, value is {date_picker.value}")

    def date_picker_dismissed(e):
        print(f"Date picker dismissed, value is {date_picker.value}")

    date_picker = ft.DatePicker(
        on_change=change_date,
        on_dismiss=date_picker_dismissed,
        first_date=datetime.datetime(2023, 10, 1),
        last_date=datetime.datetime(2024, 10, 1),
    )
    date_picker2 = ft.DatePicker(
        on_change=change_date,
        on_dismiss=date_picker_dismissed,
        first_date=datetime.datetime(2023, 10, 1),
        last_date=datetime.datetime(2024, 10, 1),
    )

    page.overlay.append(date_picker)
    page.overlay.append(date_picker2)

    date_inicio = ft.ElevatedButton(
        "Data Inicio",
        icon=ft.icons.CALENDAR_MONTH,
        width=120,
        on_click=lambda _: date_picker.pick_date(),
    )
    date_fim = ft.ElevatedButton(
        "Data Fim",
        icon=ft.icons.CALENDAR_MONTH,
        width=120,
        on_click=lambda _: date_picker2.pick_date(),
    )

    page.add(
          container,
          ft.Column([
              ft.Row([ft.Text("PRODUTO",width=120,bgcolor="blue"),produto]),
              ft.Row([ft.Text("FORNECEDOR",width=120,bgcolor="blue"),fornecedor]),
              ft.Row([ft.Text("FREQUÊNCIA",width=120,bgcolor="blue"),frequencia]),
              ft.Row([ft.Text("QUANTIDADE",width=120,bgcolor="blue"),quantidade]),
              ft.Row([date_inicio,date_fim]),cadastrar_pedido])
            


           )






    
ft.app(target=main)