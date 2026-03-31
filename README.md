# Exemple de synthèse de filtres numériques

## Filtre RII (réponse impulsionnelle infinie)

Les méthodes de synthèse de filtres numériques à réponse impulsionnelle infinie s'inspirent
directement de celles appliquées pour les filtres analogiques. On y fait notamment
appel à la
[transformation bilinéaire](https://github.com/jeanluccollette/transformee-bilineaire)
pour transposer le gabarit du filtre numérique en celui d'un filtre analogique.

On accède alors aux coefficients de la fonction de transfert qui est une fraction rationnelle.

$$H(z)=\dfrac{\sum_{m=0}^{M}b_mz^{-m}}{1+\sum_{k=1}^{K}a_kz^{-k}}=\dfrac{Y(z)}{X(z)}$$

![](data/rii_gain_db.png)

![](data/rii_gain_lin.png)

![](data/rii_phase.png)

![](data/rii_chirp.png)

## Filtre RIF (réponse impulsionnelle finie)

![](data/rif_gain_db.png)

![](data/rif_gain_lin.png)

![](data/rif_phase.png)

![](data/rif_chirp.png)
