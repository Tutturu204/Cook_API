from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.recipe import Recipe, recipe_list


class RecipeListResource(Resource):
    def get(self):

        data = []

        for recipe in recipe_list:
            if recipe.is_publish is True:
                data.append(recipe.data)

        return {"data": data}, HTTPStatus.OK

    def post(self):
        data = request.get_json()

        recipe = Recipe(name=data["name"],
                        description=data["description"],
                        num_of_servings=data["num_of_servings"],
                        cook_time=data["cook_time"],
                        directions=data["directions"]
                        )

        recipe_list.append(recipe)
        return recipe.data, HTTPStatus.CREATED


class RecipeResource(Resource):

    def get(self, recipe_id):
        for recipe in recipe_list:
            if recipe.id == recipe_id and recipe.is_publish:
                return recipe.data, HTTPStatus.OK
        return {"message": "recipe not found"}, HTTPStatus.NOT_FOUND

    def put(self, recipe_id):
        data = request.get_json()

        for recipe in recipe_list:

            if recipe.id == recipe_id:
                recipe.name = data["name"]
                recipe.description = data["description"]
                recipe.num_of_servings = data["num_of_servings"]
                recipe.cook_time = data["cook_time"]
                recipe.directions = data["directions"]

                return recipe.data, HTTPStatus.OK
        return {"message": "recipe not found"}, HTTPStatus.NOT_FOUND

    def delete(self, recipe_id):
        for recipe in recipe_list:
            if recipe.id == recipe_id:
                recipe_list.remove(recipe)
            return recipe.data, HTTPStatus.OK

        return {"message": "recipe not found"}, HTTPStatus.NOT_FOUND

class RecipePublishResource(Resource):

    def put(self, recipe_id):
        for recipe in recipe_list:
            if recipe.id == recipe_id:
                recipe.is_publish = True
                return {}, HTTPStatus.OK
        return {"message": "recipe not found"}, HTTPStatus.NOT_FOUND

    def delete(self, recipe_id):
        for recipe in recipe_list:
            if recipe.id == recipe_id:
                recipe.is_publish = False
                return {}, HTTPStatus.OK
        return {"message": "recipe not found"}, HTTPStatus.NOT_FOUND