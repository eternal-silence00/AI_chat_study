from unittest.mock import patch 

async def test_add_document(async_client):
    with patch("app.services.document_service.EmbeddingService") as mock:
        mock.return_value.get_embedding.return_value = [0.1] * 384
        response = await async_client.post("/document", json={"content":"Hello"})
        assert response.status_code == 201
        
        
async def test_get_document(async_client):
    with patch("app.services.document_service.EmbeddingService") as mock:
        mock.return_value.get_embedding.return_value = [0.1] * 384
        await async_client.post("/document", json={"content":"Hello"})
        result = await async_client.get("/document/search", params={"query":"hello", "limit":10})
        assert result.status_code == 200
        
async def test_get_document_exception(async_client):
    with patch("app.services.document_service.EmbeddingService") as mock:
        mock.return_value.get_embedding.return_value = [0.1] * 384
        result = await async_client.get("/document/search", params={"query":"hello", "limit":10})
        assert result.status_code == 404