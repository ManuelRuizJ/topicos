from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI()

df = pd.read_csv("spotify_songs.csv")
playlists = {}


@app.post("/playlists")
def crear_playlist(nombre: str):
    playlist_id = str(len(playlists) + 1)
    playlist = {
        "id": playlist_id,
        "nombre": nombre,
        "canciones": []
    }
    playlists[playlist_id] = playlist
    return playlist


@app.post("/playlists/{playlist_id}/canciones")
def agregar_cancion(playlist_id: str, id_cancion: str):
    playlist = playlists.get(playlist_id)
    if playlist is None:
        raise HTTPException(status_code=404, detail="Playlist no encontrada")

    res = df[df["track_id"] == id_cancion]
    if res.empty:
        raise HTTPException(status_code=404, detail="Cancion no encontrada")

    cancion = res.iloc[0]
    playlist["canciones"].append({
        "track_id": cancion["track_id"],
        "track_name": cancion["track_name"],
        "track_artist": cancion["track_artist"]
    })

    return playlist


@app.get("/playlists/{playlist_id}")
def consultar_playlist(playlist_id: str):
    playlist = playlists.get(playlist_id)
    if playlist is None:
        raise HTTPException(status_code=404, detail="Playlist no encontrada")

    return playlist


@app.delete("/playlists/{playlist_id}/canciones")
def eliminar_cancion(playlist_id: str, id_cancion: str):
    playlist = playlists.get(playlist_id)
    if playlist is None:
        raise HTTPException(status_code=404, detail="Playlist no encontrada")

    for cancion in playlist["canciones"]:
        if cancion["track_id"] == id_cancion:
            playlist["canciones"].remove(cancion)
            break

    return playlist


@app.delete("/playlists/{playlist_id}/canciones")
def eliminar_cancion(playlist_id: str, id_cancion: str):
    playlist = playlists.get(playlist_id)
    if playlist is None:
        raise HTTPException(status_code=404, detail="Playlist no encontrada")

    for cancion in playlist["canciones"]:
        if cancion["track_id"] == id_cancion:
            playlist["canciones"].remove(cancion)
            break
    else:
        raise HTTPException(status_code=404, detail="Cancion no encontrada en la playlist")

    return playlist


@app.get("/playlists/{playlist_id}/canciones")
def consultar_canciones(playlist_id: str, cantidad: int = 10):
    playlist = playlists.get(playlist_id)
    if playlist is None:
        raise HTTPException(status_code=404, detail="Playlist no encontrada")

    if cantidad is None:
        cantidad = 10

    return playlist["canciones"][:cantidad]


@app.get("/top-tracks")
def canciones_famosas():
    canciones = df.sort_values(by="track_popularity", ascending=False).head(10)
    return canciones[["track_id", "track_name", "track_artist", "track_popularity"]].to_dict(orient="records")


@app.patch("/playlists/{playlist_id}/canciones/{id_cancion}")
def actualizar_cancion(playlist_id: str, id_cancion: str, nuevo_nombre: str = None, nuevo_artista: str = None):
    playlist = playlists.get(playlist_id)
    if playlist is None:
        raise HTTPException(status_code=404, detail="Playlist no encontrada")

    for cancion in playlist["canciones"]:
        if cancion["track_id"] == id_cancion:
            if nuevo_nombre:
                cancion["track_name"] = nuevo_nombre
            if nuevo_artista:
                cancion["track_artist"] = nuevo_artista
            return cancion

    raise HTTPException(status_code=404, detail="Cancion no encontrada en la playlist")