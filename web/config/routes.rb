Rails.application.routes.draw do
  # For details on the DSL available within this file, see https://guides.rubyonrails.org/routing.html
  root to: 'dashboard#show'

  resources :devices do
    member do
      post 'set_static/:animation', to: 'devices#set_static'
      post 'set_random', to: 'devices#set_random'
    end
  end

end
