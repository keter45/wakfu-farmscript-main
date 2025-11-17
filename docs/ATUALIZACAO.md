# Sistema de Atualização Automática

## Como funciona

O Wakfu FarmScript agora possui um sistema de atualização automática que:

1. **Verifica** atualizações no GitHub
2. **Compara** versões (formato: X.Y.Z)
3. **Baixa** e aplica automaticamente (se for repositório git)
4. **Fallback** para download manual se necessário

## Uso

### Verificar atualizações

Clique no botão **🔄** na interface principal

### Processo de atualização

1. **Automática (Git)**:

   - Se o projeto for clonado via git
   - Faz `git pull` automaticamente
   - Preserva configurações locais (stash)
   - Solicita reinicialização do programa

2. **Manual**:
   - Abre navegador no GitHub Releases
   - Mostra instruções de atualização
   - Lista arquivos a copiar

## Configuração do GitHub

### Para criar uma release:

1. Vá em: `https://github.com/keter45/wakfu-farmscript-main/releases`
2. Clique em "Draft a new release"
3. Tag version: `v0.2.2` (sempre incremental)
4. Release title: `Wakfu FarmScript v0.2.2`
5. Descrição (changelog):

```markdown
## ✨ Novidades

- Sistema de atualização automática
- Lista completa de recursos Farmer (35 itens)
- Modo Cut-Only para Farmer/Herbalist/Lumberjack
- Marcação ✓/✗ para recursos com/sem imagem

## 🐛 Correções

- Corrigido erro ImageNotFoundException
- Ajustada região de busca para 60% da tela
- Melhorada precisão de detecção de ícones

## 📦 Melhorias

- Instalador mais robusto com verificações
- Interface reorganizada (removido campo Zona)
- Documentação completa do sistema de captcha
```

6. Clique em "Publish release"

## Formato de Versão

Seguimos **Semantic Versioning** (SemVer):

- `MAJOR.MINOR.PATCH` (ex: `0.2.1`)
- **MAJOR**: Mudanças incompatíveis
- **MINOR**: Novas funcionalidades compatíveis
- **PATCH**: Correções de bugs

### Exemplos:

- `0.2.1` → `0.2.2` = Patch (bug fix)
- `0.2.2` → `0.3.0` = Minor (nova feature)
- `0.9.0` → `1.0.0` = Major (breaking change)

## Arquivos preservados na atualização

O sistema preserva automaticamente:

- ✅ `game_area_config.json` (calibração da tela)
- ✅ `captcha_config.json` (calibração do captcha)
- ✅ `img/` (todas as imagens capturadas)
- ✅ Mudanças locais não commitadas (git stash)

## Testando localmente

```python
from src.utils.updater import updater

# Verificar atualizações
has_update, latest_version, url = updater.check_for_updates()

if has_update:
    print(f"Nova versão: {latest_version}")

    # Ver changelog
    changelog = updater.get_changelog()
    print(changelog)

    # Atualizar
    updater.update_via_git()
```

## Troubleshooting

### "Não foi possível verificar atualizações"

- Verifique conexão com internet
- GitHub pode estar fora do ar
- Tente novamente em alguns minutos

### "Git não está instalado"

- Baixe em: https://git-scm.com/downloads
- Ou use atualização manual

### "Você tem mudanças locais"

- Mudanças são preservadas automaticamente (stash)
- Para restaurar: `git stash pop`

## API do GitHub

Endpoint usado: `https://api.github.com/repos/keter45/wakfu-farmscript-main/releases/latest`

Retorna:

```json
{
	"tag_name": "v0.2.1",
	"name": "Wakfu FarmScript v0.2.1",
	"body": "Changelog markdown...",
	"zipball_url": "https://...",
	"tarball_url": "https://..."
}
```
