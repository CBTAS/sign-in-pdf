# signinpdf

Inserir assinatura (imagem: png ou jpg) em PDF por meio do PYTHON.

<br>
<p><b> Sintaxe do comando: </b> </p>
<i> signinpdf('nomedoarquivo.pdf', 'img-assinatura.png', ["Numero de paginas= int", "Posicao X= int", "Posicao Y= int", "Altura da Imagem= int", "Largura da Imagem= list[]"]) </i>
<ol><h3>Lista de argumentos:</h3>
 <li><b>'nomedoarquivo.pdf' =  </b>Informar o nome do arquivo do qual será utilizado para a inserção da imagem da assinatura;</li>
 <li><b>'img-assinatura.png' = </b>Informar o nome do arquivo da imagem da assinatura que pode estar em : png ou jpg;</li>
 <li><b> Argumento dentro de colchetes: [a, b, c, d, e] </b>
  <ul>
   <li>a. Informar o número de páginas do documento, podendo ser apenas uma página ou o tatal. O valor deve ser número inteiro;</li>
   <li>b. Informar a posicao X, com origem a partir do lado esquerdo inferior. O valor deve ser número inteiro;</li>
   <li>c. Informar a posicao Y, com origem a partir do lado esquerdo inferior. O valor deve ser número inteiro;</li>
   <li>d. Informar a altura da imagem. O valor deve ser um inteiro; </li>
   <li>e. Informar a largura da imagem. O valor deve ser um inteiro. </li>
  </ul>
</ol>
<p></p>

<br>
<p>Exemplo:</p>
<p></p>
<b>signinpdf(arquivo.pdf, img.png, [10, 300, 100, 150, 50])</b>
<br></br>
<p>Baseado nas informações:</P>
<ul>
 <li> Do projeto SIGN_PDF - Assinatura em PDF do Git do MARTINRUENZ; </li>
 <li> Do BLOG do Patrick Mazulo. (http://blog.dunderlabs.com/inserindo-informacoes-em-pdfs-editaveis.html)</li>
 <li> PyPDF2: https://pythonhosted.org/PyPDF2/</li>
</ul>
