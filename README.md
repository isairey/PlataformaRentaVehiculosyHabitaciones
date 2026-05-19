# FAER


## Models

1. Room 
```
    Attributes:
    - title             -> Char     *
    - price             -> Int      *
    - description       -> Text     *
    - home_type         -> (Room/Flat/Appartment)   *
    - room_type         -> (Single/Double/Triple/Queen/King)   * 
    - total_occupancy   -> Int
    - total_bedrooms    -> Int
    - total_bathrooms   -> Int
    - is_furnished      -> Bool
    - has_kitchen       -> Bool
    - has_internet      -> Bool
    - has_parking       -> Bool
    - has_garden        -> Bool
    - has_terrace       -> Bool
    - min_stay          -> Int
    - max_stay          -> Int
    - floor_no          -> Int
    - address           -> Char     *
    - city              -> Char
    - state             -> Char
    - zipcode           -> Int
    - latitudde         -> Decimal
    - longitude         -> Decimal
    - images            -> Dict of images 


```

2. Vehicle
```
    Attributes:
    - name              -> Char     * 
    - price             -> Int      *
    - description       -> Text     *
    - capacity          -> Int      *
    - vehicle_type      -> (Bike/Car/etc)   *
    - brand             -> Char
    - model             -> Char
    - plate_number      -> Char
    - images            -> Dict of images 

```
