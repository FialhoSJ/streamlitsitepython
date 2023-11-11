# Importando Bibliotecas
import streamlit as st
from PIL import Image
# Configurando a Página
st.set_page_config(page_title="Ciência e tecnologia")

with st.container():
    st.title("CIÊNCIA E TECNOLOGIA")
    st.write("Site dedicado ao Curso de Bacharelado em Ciência e tecnologia do IFPA.")
    st.write("---")

with st.container():
    st.title("SOBRE O CURSO:")
    st.write("O Bacharelado em Ciências e Tecnologia, do Instituto Federal do Pará – Campus Ananindeua, tem como proposta atender a comunidade de Ananindeua e adjacências, com profissionais habilitados e capacitados para trabalhar e desenvolver, sustentavelmente, a região de integração metropolitana com uso racional das ferramentas tecnológicas e atendimento tanto de atividades industriais como do campo."
    'O curso apresenta uma natureza generalista fundamentado nos conceitos de John Henry Newman, em sua obra intitulada “The Idea of a University”, a qual propõe um modelo de ensino com foco na formação do caráter dos estudantes aliada ao desenvolvimento de competências e habilidades específicas do ramo profissional escolhido. Dessa forma, a meta da formação é a de um egresso autônomo, reflexivo, letrado e socialmente engajado tanto na área de humanidades, quanto em tecnologias e ciências.'
    'O Bacharelado em Ciências e Tecnologia propõe uma aprendizagem de abrangência significativa nos campos social, científico e tecnológico, considerando, também, a própria realidade vivenciada pelo aluno, de modo que os egressos dessa categoria de curso desenvolvam competências, habilidades e conhecimentos gerais necessários ao mundo do trabalho que requerem educação superior em uma grande área do conhecimento, mas não com formação profissional específica.'
    'Sendo assim, por seu caráter generalista, o estudante poderá ao final do curso realizar estudos em nível de pós-graduação stricto sensu e/ou lato sensu ou complementar sua formação em engenharia de controle e automação, engenharia de materiais, licenciatura em matemática, licenciatura em física, licenciatura em química ou licenciatura em geografia.'
    'O curso será realizado de forma presencial, com regime letivo semestral constituído por 8 (oito) semestres letivos e estágio curricular OBRIGATÓRIO, pois, conforme a Resolução nº005/2019-CONSUP, em todos os cursos de graduação é obrigatória a previsão do estágio curricular supervisionado. O tempo mínimo de integralização do curso será em 8 (oito) semestres letivos e o máximo será de 12 (doze) semestres.')

def main():
    # Caminho da imagem
    image_path = "LOGO. png.jpg"

    # Exibir a imagem no site
    st.image(image_path, caption="Imagem Exibida", use_column_width=True)

if __name__ == "__main__":
    main()
st.write("---")
def main():
    st.title("Galeria")

    # Criar uma barra lateral para escolher a categoria
    categoria = st.sidebar.selectbox("Selecione a Categoria", ["Eventos", "Projetos"])

    # Dicionário de imagens por categoria
    imagens_por_categoria = {
        "Eventos": ["imagem 1.jpg"],
        "Projetos": ["imagem 2.jpg"],
    }

    # Obter a lista de imagens para a categoria selecionada
    imagens_da_categoria = imagens_por_categoria.get(categoria, [])

    # Adicionar um botão para a movimentação para a próxima imagem
    if imagens_da_categoria:
        index_imagem_atual = st.session_state.get('index_imagem', 0)
        if st.button("Próxima Imagem"):
            index_imagem_atual = (index_imagem_atual + 1) % len(imagens_da_categoria)
        st.image(imagens_da_categoria[index_imagem_atual], caption=f"{categoria} Exibida", use_column_width=True)
        st.session_state['index_imagem'] = index_imagem_atual

if __name__ == "__main__":
     main()
# Inserindo Links dos Artigos
st.write("---")
st.title("Artigos")
st.write("Aqui estão alguns artigos de alunos e professores do curso, que foram publicados:")
st.write("https://rsdjournal.org/index.php/rsd/article/view/24568/21645")
st.write("https://ananindeua.ifpa.edu.br/images/2023/EVENTOS/Artigo_Sicoopes2023.pdf")
st.write("https://ananindeua.ifpa.edu.br/images/2023/EVENTOS/Transio_Energtica_IVCoBICET.pdf")
st.write("https://ananindeua.ifpa.edu.br/images/2023/EVENTOS/Artigo2_Sicoopes_2023_ID.pdf")
st.write("---")




