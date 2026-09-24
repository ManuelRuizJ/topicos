from fastapi import FastAPI
import pandas as pd

app = FastAPI()

df = pd.read_csv("spotify_songs.csv")


@app.post("/crear_playlist")
def crear_playlist(nombre):
    playlist = {
        "nombre": nombre,
        "canciones": []
    }

    return playlist


@app.post("/agregar_cancion")
def agregar_cancion(playlist, id_cancion):
    res = df[df["track_id"] == id_cancion]

    if res.empty:
        print("Cancion no encontrada")
        return playlist

    cancion = res.iloc[0]

    playlist["canciones"].append({
        "track_id": cancion["track_id"],
        "track_name": cancion["track_name"],
        "track_artist": cancion["track_artist"]
    })
    
    return playlist


@app.get("/consultar_playlist")
def consultar_playlist(playlist):
    print(f"Playlist: {playlist['nombre']}")
    print(f"Total de canciones: {len(playlist['canciones'])}")
    
    for i, cancion in enumerate(playlist["canciones"], 1):
        print(f"{i}. {cancion['track_name']} - {cancion['track_artist']}")


@app.post("/eliminar_cancion")
def eliminar_cancion(playlist, id_cancion):
    for cancion in playlist["canciones"]:
        if cancion["track_id"] == id_cancion:
            playlist["canciones"].remove(cancion)

    return playlist


@app.get("/consultar_canciones")
def consultar_canciones(cantidad= 10):
    if cantidad is None:
        cantidad = 10
    return df[["track_name", "track_artist", "playlist_genre", "track_popularity"]].sort_values(
                by="track_popularity",
                ascending=False
            ).head(cantidad)
