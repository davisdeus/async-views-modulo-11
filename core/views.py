import asyncio
from django.http import JsonResponse

async def contador(request):
    passos = []
    for i in range(1, 6):
        await asyncio.sleep(1)
        passos.append(f"{i} segundo(s)")
    return JsonResponse({"mensagem": "Contagem concluída", "passos": passos})
