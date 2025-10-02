document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("analysis-form");
  const statusDiv = document.getElementById("status");
  const resultadoDiv = document.getElementById("resultado");

  form.addEventListener("submit", async function (event) {
    event.preventDefault();

    statusDiv.textContent = "Enviando arquivo...";
    resultadoDiv.style.display = "none";
    resultadoDiv.innerHTML = "";

    const fileData = new FormData();
    fileData.append("file", document.getElementById("file-input").files[0]);

    try {
      const uploadResponse = await fetch("/files", {
        method: "POST",
        body: fileData,
      });

      const uploadResult = await uploadResponse.json();

      if (!uploadResponse.ok) {
        throw new Error(uploadResult.erro || "Erro no upload do arquivo.");
      }

      const fileId = uploadResult.file_id;
      statusDiv.textContent = `Arquivo enviado com sucesso (ID: ${fileId}). Analisando...`;

      const analysisData = new FormData(form);
      analysisData.delete("file");

      const analysisResponse = await fetch(`/files/${fileId}/analysis`, {
        method: "POST",
        body: analysisData,
      });

      const analysisResult = await analysisResponse.json();

      if (!analysisResponse.ok) {
        throw new Error(analysisResult.erro || "Erro ao analisar o arquivo.");
      }
      statusDiv.textContent = "Análise concluída!";
      resultadoDiv.style.display = "block";
      resultadoDiv.innerHTML = `
        <h3>Resultados da Análise:</h3>
        <ul>
          <li><strong>Receita Total:</strong> ${analysisResult.receita_total.toLocaleString(
            "pt-BR",
            { style: "currency", currency: "BRL" }
          )}</li>
          <li><strong>Produto Mais Vendido:</strong> ${
            analysisResult.produtos_mais_vendidos
          }</li>
          <li><strong>Cliente com Maior Gasto (ID):</strong> ${
            analysisResult.cliente_com_maior_gasto
          }</li>
          <li><strong>Total de Transações:</strong> ${
            analysisResult.total_transacoes
          }</li>
        </ul>
      `;
    } catch (error) {
      statusDiv.textContent = "Ocorreu um erro:";
      resultadoDiv.style.display = "block";
      resultadoDiv.innerHTML = `<p style="color: red;">${error.message}</p>`;
    }
  });
});
